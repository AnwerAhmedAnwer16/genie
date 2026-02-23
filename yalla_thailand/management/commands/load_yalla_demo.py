#!/usr/bin/env python3
"""
Load Yalla Thailand full demo data.

Creates:
- 4 Thai Destinations (Bangkok, Krabi, Phi Phi, Phuket)
- 100 Hotels (25 per destination) from CSV files
- Thai airlines, tour sites, transport suppliers, room types
- Trip packages from CSV (Trips Sheet - Trips.csv) with all fields
- 20 Tour Bookings with flights, hotels, transports, programs, insurance, documents
- Sales Orders linked to confirmed/booked bookings
- Purchase Orders linked to bookings (for suppliers)

Usage:
    python manage.py load_yalla_demo
    python manage.py load_yalla_demo --dry-run
    python manage.py load_yalla_demo --clear
"""

import csv
import random
import string
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from math import ceil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from modules.base.middleware import company_context, branch_context
from modules.base.models import Partner, User, Country, Company, Currency, Branch
from modules.tourism.models import (
    Destination, TourSite, RoomType, PackageType, TourPackage,
    TourPackageFlightItem, TourPackageHotelItem,
    TourPackageTransportItem, TourPackageProgramItem,
    TourBooking, FlightSegment, HotelBooking,
    TransportBooking, TourProgram, PassportVisa, TourInsurance,
)

HOTELS_PER_DEST = 25

CSV_DESTINATION_MAP = {
    'All Hotels - Bangkok Hotels.csv': {
        'name': 'Bangkok', 'code': 'BKK', 'type': 'airport',
    },
    'All Hotels - Krabi Hotels.csv': {
        'name': 'Krabi', 'code': 'KBV', 'type': 'airport',
    },
    'All Hotels - Phi Phi Hotels.csv': {
        'name': 'Phi Phi Islands', 'code': 'PHI', 'type': 'city',
    },
    'All Hotels - Phuket Hotels.csv': {
        'name': 'Phuket', 'code': 'HKT', 'type': 'airport',
    },
}

THAI_AIRLINES = [
    {'name': 'Thai Airways', 'code': 'TG'},
    {'name': 'Bangkok Airways', 'code': 'PG'},
    {'name': 'Thai AirAsia', 'code': 'FD'},
    {'name': 'Nok Air', 'code': 'DD'},
    {'name': 'Thai Lion Air', 'code': 'SL'},
    {'name': 'Thai Smile Airways', 'code': 'WE'},
]

THAI_TOUR_SITES = {
    'BKK': [
        {'name': 'Grand Palace', 'desc': 'Historic royal palace complex on the Chao Phraya River'},
        {'name': 'Wat Pho', 'desc': 'Temple of the Reclining Buddha'},
        {'name': 'Wat Arun', 'desc': 'Temple of Dawn with porcelain-decorated spires'},
        {'name': 'Chatuchak Weekend Market', 'desc': 'One of the largest outdoor markets in the world'},
        {'name': 'Khao San Road', 'desc': 'Famous backpacker street with vibrant nightlife'},
        {'name': 'Jim Thompson House', 'desc': 'Museum showcasing Thai art and architecture'},
        {'name': 'Chinatown (Yaowarat)', 'desc': 'Vibrant district with street food and gold shops'},
        {'name': 'MBK Center', 'desc': 'Iconic shopping mall'},
    ],
    'KBV': [
        {'name': 'Railay Beach', 'desc': 'Stunning limestone cliffs and pristine beach'},
        {'name': 'Tiger Cave Temple', 'desc': 'Buddhist temple with 1,237 steps to the summit'},
        {'name': 'Ao Nang Beach', 'desc': 'Popular beach town and gateway to islands'},
        {'name': 'Emerald Pool', 'desc': 'Natural crystal-clear pool in the rainforest'},
        {'name': 'Hong Islands', 'desc': 'Group of islands with lagoons and snorkeling'},
        {'name': 'Thung Teao Forest Park', 'desc': 'Tropical forest with Blue Pool and nature trails'},
    ],
    'PHI': [
        {'name': 'Maya Bay', 'desc': 'Famous beach from "The Beach" movie'},
        {'name': 'Phi Phi Viewpoint', 'desc': 'Panoramic view of Tonsai and Loh Dalum bays'},
        {'name': 'Monkey Beach', 'desc': 'Beach with monkeys, great for snorkeling'},
        {'name': 'Viking Cave', 'desc': 'Cave with ancient paintings'},
        {'name': 'Bamboo Island', 'desc': 'Small island with white sand and coral reefs'},
        {'name': 'Loh Samah Bay', 'desc': 'Sheltered bay for snorkeling and diving'},
    ],
    'HKT': [
        {'name': 'Patong Beach', 'desc': 'Most popular beach with nightlife and water sports'},
        {'name': 'Big Buddha', 'desc': '45-meter tall white marble Buddha on Nakkerd Hill'},
        {'name': 'Phuket Old Town', 'desc': 'Historic Sino-Portuguese architecture and street art'},
        {'name': 'Kata Beach', 'desc': 'Beautiful beach popular with families and surfers'},
        {'name': 'Phang Nga Bay', 'desc': 'Dramatic limestone karsts, James Bond Island'},
        {'name': 'Promthep Cape', 'desc': 'Southernmost tip of Phuket, famous sunset viewpoint'},
        {'name': 'Wat Chalong', 'desc': 'Most important Buddhist temple in Phuket'},
        {'name': 'Similan Islands', 'desc': 'World-class diving and snorkeling destination'},
    ],
}

THAI_TRANSPORT_SUPPLIERS = [
    'Bangkok Shuttle Service',
    'Phuket Airport Transfer',
    'Krabi Taxi & Tours',
    'Thailand Van Service',
    'Phi Phi Ferry Express',
    'Andaman Sea Transport',
]

THAI_ROOM_TYPES = [
    {'name': 'Standard Room', 'capacity': 2},
    {'name': 'Superior Room', 'capacity': 2},
    {'name': 'Deluxe Room', 'capacity': 2},
    {'name': 'Pool Villa', 'capacity': 4},
    {'name': 'Beachfront Bungalow', 'capacity': 2},
    {'name': 'Family Suite', 'capacity': 4},
    {'name': 'Presidential Suite', 'capacity': 4},
]

CUSTOMERS = [
    {'name': 'Ahmad Al-Mansour', 'email': 'ahmad.mansour@yalla.com', 'phone': '+971-50-111-2233'},
    {'name': 'Fatima Al-Rashid', 'email': 'fatima.rashid@yalla.com', 'phone': '+971-55-222-3344'},
    {'name': 'Khalid Al-Sabah', 'email': 'khalid.sabah@yalla.com', 'phone': '+966-50-333-4455'},
    {'name': 'Noura Al-Thani', 'email': 'noura.thani@yalla.com', 'phone': '+974-55-444-5566'},
    {'name': 'Omar Hassan', 'email': 'omar.hassan@yalla.com', 'phone': '+20-100-555-6677'},
    {'name': 'Leila Boutros', 'email': 'leila.boutros@yalla.com', 'phone': '+961-70-666-7788'},
    {'name': 'Youssef Karim', 'email': 'youssef.karim@yalla.com', 'phone': '+971-56-777-8899'},
    {'name': 'Maryam Jawad', 'email': 'maryam.jawad@yalla.com', 'phone': '+973-33-888-9900'},
    {'name': 'Sami Nasser', 'email': 'sami.nasser@yalla.com', 'phone': '+965-66-999-0011'},
    {'name': 'Hana Farid', 'email': 'hana.farid@yalla.com', 'phone': '+971-52-000-1122'},
    {'name': 'Rami Khalil', 'email': 'rami.khalil@yalla.com', 'phone': '+962-79-111-2233'},
    {'name': 'Dina Mahmoud', 'email': 'dina.mahmoud@yalla.com', 'phone': '+20-111-333-4455'},
    {'name': 'Tariq Al-Farsi', 'email': 'tariq.farsi@yalla.com', 'phone': '+968-99-555-6677'},
    {'name': 'Salma Osman', 'email': 'salma.osman@yalla.com', 'phone': '+249-91-777-8899'},
    {'name': 'Ali Reda', 'email': 'ali.reda@yalla.com', 'phone': '+971-58-999-0011'},
]

# Map category_01 to destination codes for bookings
CATEGORY_DEST_MAP = {
    'Phi Phi': 'HKT',
    'James Bond': 'HKT',
    'Krabi': 'KBV',
    'Similan': 'HKT',
    'Adventures': 'HKT',
    'Night Shows': 'HKT',
    'Raya & Coral': 'HKT',
    'Private Boats': 'HKT',
}


def _safe_decimal(val, default=Decimal('0')):
    """Parse a string to Decimal, returning default on failure."""
    if not val or not str(val).strip():
        return default
    try:
        cleaned = str(val).strip().replace(',', '')
        return Decimal(cleaned)
    except (InvalidOperation, ValueError):
        return default


class Command(BaseCommand):
    help = 'Load Yalla Thailand full demo data (hotels, bookings, SO, PO, packages from CSV)'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Preview without creating')
        parser.add_argument('--clear', action='store_true', help='Clear existing yalla demo data first')

    def handle(self, *args, **options):
        self.dry_run = options['dry_run']

        if self.dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN MODE'))

        company, branch = self._setup_env()
        if not company:
            return

        try:
            with transaction.atomic():
                if options['clear']:
                    self._clear_demo_data()

                user = User.objects.filter(is_superuser=True).first() or User.objects.first()
                if not user:
                    self.stdout.write(self.style.ERROR('No user found'))
                    return

                currency = Currency.objects.first()

                # 1. Infrastructure
                thailand = self._create_country(user)
                destinations = self._create_destinations(thailand, user)
                hotels_by_dest = self._load_hotels(destinations, user)
                sites_by_dest = self._create_tour_sites(destinations, user)
                airlines = self._create_airlines(user)
                transport_suppliers = self._create_transport_suppliers(user)
                room_types = self._create_room_types(user)
                customers = self._create_customers(user)
                insurance_providers = self._create_insurance_providers(user)

                # 2. Package Types & Packages from CSV
                package_types = self._create_package_types(user)
                csv_trips = self._read_trips_csv()
                trip_suppliers = self._create_trip_suppliers(csv_trips, user)
                packages = self._create_tour_packages_from_csv(
                    user, branch, csv_trips, trip_suppliers, package_types
                )

                # 3. Bookings
                bookings = self._create_bookings(
                    user, branch, currency, destinations, airlines,
                    hotels_by_dest, room_types, transport_suppliers,
                    sites_by_dest, customers, insurance_providers, packages
                )

                # 4. Sales Orders
                sales_orders = self._create_sales_orders(user, branch, currency, bookings, customers)

                # 5. Purchase Orders
                purchase_orders = self._create_purchase_orders(
                    user, branch, bookings, hotels_by_dest, airlines, transport_suppliers
                )

                self._print_summary(
                    destinations, hotels_by_dest, airlines, transport_suppliers,
                    package_types, packages, bookings, sales_orders, purchase_orders
                )

                if self.dry_run:
                    raise _DryRunAbort()

        except _DryRunAbort:
            self.stdout.write(self.style.WARNING('\nDry run complete - no changes saved'))
        finally:
            self._cleanup_env()

    # =========================================================================
    # Environment
    # =========================================================================

    def _setup_env(self):
        company = Company.objects.first()
        if not company:
            self.stdout.write(self.style.ERROR('No company found'))
            return None, None
        branch = company.headquarters
        if not branch:
            self.stdout.write(self.style.ERROR('No headquarters branch'))
            return None, None
        company_context.set(company.id)
        branch_context.set([branch.id])
        self.stdout.write(self.style.SUCCESS(f'Environment: {company.name} / {branch.name}'))
        return company, branch

    def _cleanup_env(self):
        company_context.set(None)
        branch_context.set(None)

    # =========================================================================
    # Clear
    # =========================================================================

    def _clear_demo_data(self):
        self.stdout.write('\nClearing yalla demo data...')

        # Delete bookings tagged with yalla customers
        yalla_emails = [c['email'] for c in CUSTOMERS]
        yalla_partners = Partner.objects.filter(email__in=yalla_emails)
        bookings = TourBooking.objects.filter(partner__in=yalla_partners)
        bc = bookings.count()
        if bc:
            from modules.sales.models.order import SalesOrder
            from modules.purchase.models import Order as PurchaseOrder
            SalesOrder.objects.filter(tour_booking__in=bookings).delete()
            PurchaseOrder.objects.filter(tour_booking__in=bookings).delete()
            bookings.delete()
        self.stdout.write(f'  Bookings deleted: {bc}')

        # Delete packages created from CSV
        pc = TourPackage.objects.filter(name__startswith='Yalla Thailand').count()
        TourPackage.objects.filter(name__startswith='Yalla Thailand').delete()
        # Also delete CSV-based trip packages
        pc2 = TourPackage.objects.filter(category_01__isnull=False).exclude(category_01='').count()
        TourPackage.objects.filter(category_01__isnull=False).exclude(category_01='').delete()
        self.stdout.write(f'  Packages deleted: {pc + pc2}')

        # Delete yalla hotels
        hc = Partner.objects.filter(is_hotel=True, email__endswith='@yalla-thailand-hotels.com').count()
        if hc:
            Partner.objects.filter(is_hotel=True, email__endswith='@yalla-thailand-hotels.com').delete()
        self.stdout.write(f'  Hotels deleted: {hc}')

        # Delete yalla customers
        Partner.objects.filter(email__in=yalla_emails).delete()

        # Delete thai airlines
        codes = [a['code'] for a in THAI_AIRLINES]
        Partner.objects.filter(is_airline=True, airline_code__in=codes).delete()

        # Delete transport suppliers
        Partner.objects.filter(name__in=THAI_TRANSPORT_SUPPLIERS).delete()

        # Delete trip suppliers
        Partner.objects.filter(email__endswith='@yalla-trip-suppliers.com').delete()

        # Delete insurance providers
        Partner.objects.filter(email__endswith='@insurance-th.com').delete()

        # Delete tour sites for thai destinations
        thai_codes = [d['code'] for d in CSV_DESTINATION_MAP.values()]
        TourSite.objects.filter(destination__code__in=thai_codes).delete()

        # Delete package types
        PackageType.objects.filter(name='Thailand Tours').delete()
        PackageType.objects.filter(
            name__in=['Beach & Relaxation', 'Island Hopping', 'City & Culture',
                      'Adventure & Diving', 'Luxury & Wellness', 'Multi-Destination']
        ).delete()

        self.stdout.write(self.style.SUCCESS('  Clear complete'))

    # =========================================================================
    # 1. Infrastructure
    # =========================================================================

    def _create_country(self, user):
        thailand, created = Country.objects.get_or_create(code='TH', defaults={'name': 'Thailand'})
        self.stdout.write(f'\n{"Created" if created else "Found"} country: Thailand')
        return thailand

    def _create_destinations(self, thailand, user):
        self.stdout.write('\nCreating Thai destinations...')
        destinations = {}
        for dest_info in CSV_DESTINATION_MAP.values():
            dest, created = Destination.objects.get_or_create(
                code=dest_info['code'],
                defaults={'name': dest_info['name'], 'country': thailand,
                          'destination_type': dest_info['type'], 'created_by': user}
            )
            destinations[dest_info['code']] = dest
            self.stdout.write(f'  {"+" if created else "="} {dest.name} ({dest.code})')
        return destinations

    def _load_hotels(self, destinations, user):
        self.stdout.write(f'\nLoading {HOTELS_PER_DEST} hotels per destination...')
        demo_dir = Path(settings.BASE_DIR) / 'yalla_demo'
        hotels_by_dest = {}

        for csv_file, dest_info in CSV_DESTINATION_MAP.items():
            csv_path = demo_dir / csv_file
            code = dest_info['code']
            hotels_by_dest[code] = []

            if not csv_path.exists():
                self.stdout.write(self.style.WARNING(f'  Missing: {csv_file}'))
                continue

            count = 0
            with open(csv_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if count >= HOTELS_PER_DEST:
                        break
                    name = line.strip().strip('"')
                    if not name:
                        continue

                    slug = (name.lower().replace(' ', '-').replace("'", '')
                            .replace('"', '').replace('&', 'and').replace(',', '')
                            .replace('/', '-').replace('(', '').replace(')', '').replace('@', 'at'))
                    email = f'{slug[:200]}@yalla-thailand-hotels.com'

                    hotel, _ = Partner.objects.get_or_create(
                        name=name, email=email,
                        defaults={'is_hotel': True, 'created_by': user}
                    )
                    hotels_by_dest[code].append(hotel)
                    count += 1

            self.stdout.write(f'  {dest_info["name"]}: {count} hotels')
        return hotels_by_dest

    def _create_tour_sites(self, destinations, user):
        self.stdout.write('\nCreating tour sites...')
        sites_by_dest = {}
        total = 0
        for code, sites_data in THAI_TOUR_SITES.items():
            dest = destinations.get(code)
            if not dest:
                continue
            sites_by_dest[code] = []
            for s in sites_data:
                site, created = TourSite.objects.get_or_create(
                    name=s['name'], destination=dest,
                    defaults={'description': s['desc'], 'created_by': user}
                )
                sites_by_dest[code].append(site)
                if created:
                    total += 1
        self.stdout.write(f'  Tour sites: {total} created')
        return sites_by_dest

    def _create_airlines(self, user):
        self.stdout.write('\nCreating Thai airlines...')
        airlines = {}
        for a in THAI_AIRLINES:
            airline, _ = Partner.objects.get_or_create(
                name=a['name'],
                defaults={'is_airline': True, 'airline_code': a['code'], 'created_by': user}
            )
            airlines[a['code']] = airline
        self.stdout.write(f'  Airlines: {len(airlines)}')
        return airlines

    def _create_transport_suppliers(self, user):
        self.stdout.write('\nCreating transport suppliers...')
        suppliers = []
        for name in THAI_TRANSPORT_SUPPLIERS:
            s, _ = Partner.objects.get_or_create(
                name=name,
                defaults={'is_transport_provider': True,
                          'email': f'{name.lower().replace(" ", ".")}@transport-th.com',
                          'created_by': user}
            )
            suppliers.append(s)
        self.stdout.write(f'  Transport suppliers: {len(suppliers)}')
        return suppliers

    def _create_room_types(self, user):
        self.stdout.write('\nEnsuring room types...')
        room_types = []
        for rt in THAI_ROOM_TYPES:
            obj, _ = RoomType.objects.get_or_create(
                name=rt['name'], defaults={'capacity': rt['capacity'], 'created_by': user}
            )
            room_types.append(obj)
        self.stdout.write(f'  Room types: {len(room_types)}')
        return room_types

    def _create_customers(self, user):
        self.stdout.write('\nCreating customers...')
        customers = []
        for c in CUSTOMERS:
            partner, _ = Partner.objects.get_or_create(
                email=c['email'],
                defaults={'name': c['name'], 'phone': c['phone'], 'created_by': user}
            )
            customers.append(partner)
        self.stdout.write(f'  Customers: {len(customers)}')
        return customers

    def _create_insurance_providers(self, user):
        self.stdout.write('\nCreating insurance providers...')
        names = ['Thailand Travel Insurance Co.', 'Allianz Travel Thailand', 'AXA Assistance Thailand']
        providers = []
        for name in names:
            p, _ = Partner.objects.get_or_create(
                name=name,
                defaults={'email': f'{name.lower().replace(" ", ".")}@insurance-th.com',
                          'created_by': user}
            )
            providers.append(p)
        self.stdout.write(f'  Insurance providers: {len(providers)}')
        return providers

    # =========================================================================
    # 2. Package Types & Packages from CSV
    # =========================================================================

    def _create_package_types(self, user):
        self.stdout.write('\nCreating package types...')
        parent = PackageType.objects.create(
            name='Thailand Tours', description='Thailand tour packages',
            color='#FF6B35', sequence=1, created_by=user
        )
        children_data = [
            {'name': 'Beach & Relaxation', 'color': '#00BCD4', 'seq': 10},
            {'name': 'Island Hopping', 'color': '#4CAF50', 'seq': 20},
            {'name': 'City & Culture', 'color': '#9C27B0', 'seq': 30},
            {'name': 'Adventure & Diving', 'color': '#FF9800', 'seq': 40},
            {'name': 'Luxury & Wellness', 'color': '#E91E63', 'seq': 50},
            {'name': 'Multi-Destination', 'color': '#2196F3', 'seq': 60},
        ]
        types = {'Thailand Tours': parent}
        for c in children_data:
            pt = PackageType.objects.create(
                name=c['name'], parent=parent, color=c['color'],
                sequence=c['seq'], created_by=user
            )
            types[c['name']] = pt
        self.stdout.write(f'  Package types: {len(types)}')
        return types

    def _read_trips_csv(self):
        """Read all trips from the Trips Sheet CSV file."""
        self.stdout.write('\nReading trips CSV...')
        demo_dir = Path(settings.BASE_DIR) / 'yalla_demo'
        csv_path = demo_dir / 'Trips Sheet - Trips.csv'

        if not csv_path.exists():
            self.stdout.write(self.style.WARNING(f'  Missing: {csv_path}'))
            return []

        trips = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                trip = {
                    'seq': row.get('S', '').strip(),
                    'trip_name': row.get('Trip Name', '').strip(),
                    'category_01': row.get('Category.01', '').strip(),
                    'category_02': row.get('Category.02', '').strip(),
                    'category_03': row.get('Category.03', '').strip(),
                    'selling_price': _safe_decimal(row.get('Selling PRC', '')),
                    'min_selling': _safe_decimal(row.get('Min Selling', '')),
                    'net_price': _safe_decimal(row.get('Net PRC', '')),
                    'supplier': row.get('Supplier', '').strip(),
                    'duration': row.get('Duration', '').strip(),
                    'short_description': row.get('Short Description', '').strip(),
                    'kids_friendly': bool(row.get('Kids friendly', '').strip()),
                    'action_adrenaline': bool(row.get('Action Adrenaline', '').strip()),
                    'family_friendly': bool(row.get('Family Friendly', '').strip()),
                    'romantic_honeymoon': bool(row.get('Romantic/\nHoneymoon', row.get('Romantic/Honeymoon', '')).strip()),
                    'smoker_friendly': bool(row.get('Smoker Friendly', '').strip()),
                    'whatsapp_catalog_link': row.get('WhatsApp Catalog Link', '').strip(),
                    'video': row.get('Video', '').strip(),
                    'album': row.get('Album', '').strip(),
                }
                if trip['trip_name']:
                    trips.append(trip)

        self.stdout.write(f'  Trips loaded from CSV: {len(trips)}')
        return trips

    def _create_trip_suppliers(self, csv_trips, user):
        """Create Partner records for each unique supplier in the CSV."""
        self.stdout.write('\nCreating trip suppliers from CSV...')
        supplier_names = set()
        for trip in csv_trips:
            if trip['supplier']:
                supplier_names.add(trip['supplier'])

        suppliers = {}
        for name in sorted(supplier_names):
            slug = name.lower().replace(' ', '.').replace("'", '').replace('(', '').replace(')', '')
            email = f'{slug[:200]}@yalla-trip-suppliers.com'
            partner, _ = Partner.objects.get_or_create(
                name=name,
                defaults={'email': email, 'created_by': user}
            )
            suppliers[name] = partner

        self.stdout.write(f'  Trip suppliers: {len(suppliers)}')
        return suppliers

    def _get_package_type_for_category(self, category_01, package_types):
        """Map CSV category_01 to a PackageType."""
        mapping = {
            'Phi Phi': 'Island Hopping',
            'James Bond': 'Island Hopping',
            'Krabi': 'Adventure & Diving',
            'Similan': 'Island Hopping',
            'Adventures': 'Adventure & Diving',
            'Night Shows': 'City & Culture',
            'Raya & Coral': 'Beach & Relaxation',
            'Private Boats': 'Luxury & Wellness',
        }
        pt_name = mapping.get(category_01, 'Thailand Tours')
        return package_types.get(pt_name)

    def _create_tour_packages_from_csv(self, user, branch, csv_trips, trip_suppliers, package_types):
        """Create TourPackage records from CSV trip data, mapping all columns."""
        self.stdout.write('\nCreating tour packages from CSV trips...')

        packages = []
        for trip in csv_trips:
            supplier_partner = trip_suppliers.get(trip['supplier'])
            pkg_type = self._get_package_type_for_category(trip['category_01'], package_types)

            # Map duration text to days
            duration_text = trip['duration'].lower()
            if 'full day' in duration_text:
                duration_days = 1
            elif 'half day' in duration_text:
                duration_days = 1
            elif 'evening' in duration_text or 'afternoon' in duration_text:
                duration_days = 1
            else:
                duration_days = 1

            package = TourPackage.objects.create(
                # Existing TourPackage fields
                name=trip['trip_name'],
                description=trip['short_description'],
                package_type=pkg_type,
                is_active=True,
                default_duration_days=duration_days,
                base_price=trip['selling_price'],
                package_seats=random.randint(20, 50),
                remaining_seats=random.randint(5, 30),
                branch=branch,
                created_by=user,
                # Yalla extension fields
                category_01=trip['category_01'],
                category_02=trip['category_02'],
                category_03=trip['category_03'],
                min_selling_price=trip['min_selling'] if trip['min_selling'] else None,
                net_price=trip['net_price'] if trip['net_price'] else None,
                supplier=supplier_partner,
                duration_type=trip['duration'],
                kids_friendly=trip['kids_friendly'],
                action_adrenaline=trip['action_adrenaline'],
                family_friendly=trip['family_friendly'],
                romantic_honeymoon=trip['romantic_honeymoon'],
                smoker_friendly=trip['smoker_friendly'],
                whatsapp_catalog_link=trip['whatsapp_catalog_link'],
                video_link=trip['video'],
                album=trip['album'],
            )
            packages.append(package)

        self.stdout.write(self.style.SUCCESS(f'  Tour packages created: {len(packages)}'))
        return packages

    # =========================================================================
    # 3. Bookings
    # =========================================================================

    def _create_bookings(self, user, branch, currency, destinations, airlines,
                         hotels_by_dest, room_types, transport_suppliers,
                         sites_by_dest, customers, insurance_providers, packages):
        self.stdout.write('\nCreating 20 tour bookings...')

        state_queue = (
            ['draft'] * 3 + ['in_process'] * 3 + ['confirmed'] * 5 +
            ['booked'] * 4 + ['completed'] * 4 + ['cancelled'] * 1
        )
        random.shuffle(state_queue)

        # Ensure DXB origin exists
        dxb = Destination.objects.filter(code='DXB').first()

        bookings = []
        # Pick 20 random packages for bookings
        booking_packages = random.sample(packages, min(20, len(packages))) if len(packages) >= 20 else packages[:20]

        for i in range(min(20, len(booking_packages))):
            pkg = booking_packages[i]
            state = state_queue[i]

            # Determine destination from category
            dest_code = CATEGORY_DEST_MAP.get(pkg.category_01, 'HKT')
            dest = destinations.get(dest_code)
            dest_name = f'{pkg.category_01}, Thailand' if pkg.category_01 else 'Phuket, Thailand'

            # Duration from package
            duration = pkg.default_duration_days or 1
            adults = random.choice([2, 2, 2, 3, 4])
            children = random.choice([0, 0, 0, 1, 2])
            infants = 0 if children == 0 else random.choice([0, 0, 1])
            travel_class = 'business' if (pkg.base_price or 0) > 4000 else 'economy'

            if state == 'completed':
                start = date.today() - timedelta(days=random.randint(10, 90))
            elif state == 'cancelled':
                start = date.today() + timedelta(days=random.randint(-20, 30))
            elif state in ['draft', 'in_process']:
                start = date.today() + timedelta(days=random.randint(30, 180))
            else:
                start = date.today() + timedelta(days=random.randint(7, 60))

            end = start + timedelta(days=duration)
            customer = random.choice(customers)

            booking = TourBooking.objects.create(
                partner=customer, destination=dest_name,
                start_date=start, end_date=end,
                adults_count=adults, children_count=children,
                infants_count=infants,
                currency=currency, sales_person=user, branch=branch,
                state=state, package=pkg,
                notes=f'{pkg.name} | Supplier: {pkg.supplier.name if pkg.supplier else "N/A"} | Sell: {pkg.base_price} THB | Net: {pkg.net_price or "N/A"} THB',
                created_by=user,
            )

            # Flights
            airline = random.choice(list(airlines.values())) if airlines else None
            if airline and dest and dxb:
                pnr = ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))
                base = Decimal('850') if travel_class == 'economy' else Decimal('2500')
                FlightSegment.objects.create(
                    booking=booking, pnr=pnr, sequence=10, airline=airline,
                    flight_number=f'{airline.airline_code}{random.randint(100,999)}',
                    from_destination=dxb, to_destination=dest, travel_class=travel_class,
                    departure_date=timezone.make_aware(timezone.datetime.combine(start, timezone.datetime.min.time().replace(hour=8))),
                    arrival_date=timezone.make_aware(timezone.datetime.combine(start, timezone.datetime.min.time().replace(hour=16))),
                    adult_price=base * Decimal(str(random.uniform(0.9, 1.1))),
                    child_price=base * Decimal('0.75'), infant_price=base * Decimal('0.10'),
                    created_by=user,
                )
                FlightSegment.objects.create(
                    booking=booking, pnr=pnr, sequence=20, airline=airline,
                    flight_number=f'{airline.airline_code}{random.randint(100,999)}',
                    from_destination=dest, to_destination=dxb, travel_class=travel_class,
                    departure_date=timezone.make_aware(timezone.datetime.combine(end, timezone.datetime.min.time().replace(hour=14))),
                    arrival_date=timezone.make_aware(timezone.datetime.combine(end, timezone.datetime.min.time().replace(hour=22))),
                    adult_price=base * Decimal(str(random.uniform(0.9, 1.1))),
                    child_price=base * Decimal('0.75'), infant_price=base * Decimal('0.10'),
                    created_by=user,
                )

            # Hotel
            dest_hotels = hotels_by_dest.get(dest_code, [])
            hotel = random.choice(dest_hotels) if dest_hotels else None
            room = random.choice(room_types) if room_types else None
            if hotel and room and dest:
                total_guests = adults + children
                HotelBooking.objects.create(
                    booking=booking, hotel=hotel, destination=dest, room_type=room,
                    checkin_date=start, checkout_date=end,
                    rooms_required=max(1, ceil(total_guests / 2)),
                    nightly_rate=Decimal(str(random.randint(80, 350))),
                    breakfast_included=True,
                    cost_price=Decimal(str(random.randint(50, 250))) * duration,
                    created_by=user,
                )

            # Transport (non-draft)
            if state != 'draft':
                supplier = random.choice(transport_suppliers) if transport_suppliers else None
                if supplier:
                    TransportBooking.objects.create(
                        booking=booking, transport_type='van', vehicle_name='Airport Transfer Van',
                        from_location='Airport', to_location='Hotel',
                        journey_date=timezone.make_aware(timezone.datetime.combine(start, timezone.datetime.min.time().replace(hour=17))),
                        price_per_person=Decimal('25.00'), supplier=supplier, created_by=user,
                    )
                    TransportBooking.objects.create(
                        booking=booking, transport_type='van', vehicle_name='Airport Transfer Van',
                        from_location='Hotel', to_location='Airport',
                        journey_date=timezone.make_aware(timezone.datetime.combine(end, timezone.datetime.min.time().replace(hour=10))),
                        price_per_person=Decimal('25.00'), supplier=supplier, created_by=user,
                    )

            # Programs (confirmed+)
            if state not in ['draft', 'in_process']:
                dest_sites = sites_by_dest.get(dest_code, [])
                for day in range(1, duration + 1):
                    prog = TourProgram.objects.create(
                        booking=booking, day_number=day,
                        program_date=start + timedelta(days=day - 1),
                        title=f'Day {day}: {"Arrival" if day == 1 else "Departure" if day == duration else "Excursion"}',
                        description=f'Day {day} activities',
                        breakfast=day > 1, lunch=day not in [1, duration], dinner=True,
                        price_per_person=Decimal(str(random.randint(20, 100))),
                        created_by=user,
                    )
                    if dest_sites and day not in [1, duration]:
                        prog.sites.add(*random.sample(dest_sites, min(2, len(dest_sites))))

            # Passport
            PassportVisa.objects.create(
                booking=booking, document_type='passport', passenger_name=customer.name,
                passport_number=f'TH{random.randint(100000, 999999)}',
                application_date=date.today() - timedelta(days=random.randint(30, 60)),
                state='delivered' if state in ['confirmed', 'booked', 'completed'] else 'draft',
                created_by=user,
            )

            # Insurance (non-draft, non-cancelled)
            if state not in ['draft', 'cancelled']:
                provider = random.choice(insurance_providers)
                base_prem = Decimal('50') * (Decimal(str(duration)) / Decimal('7'))
                insurance = TourInsurance.objects.create(
                    policy_number=f'YTH-2026-{10000 + i}',
                    insurance_provider=provider, coverage_amount=Decimal('100000'),
                    coverage_start=start - timedelta(days=1), coverage_end=end + timedelta(days=1),
                    adult_premium=base_prem, child_premium=base_prem * Decimal('0.5'),
                    infant_premium=base_prem * Decimal('0.2'), created_by=user,
                )
                booking.insurance = insurance
                booking.save(update_fields=['insurance'])

            booking.compute_totals_from_bookings()
            bookings.append(booking)
            self.stdout.write(f'  + #{booking.name} | {dest_name[:25]} | {state} | {adults}A {children}C | {pkg.name[:30]}')

        self.stdout.write(self.style.SUCCESS(f'  Total bookings: {len(bookings)}'))
        return bookings

    # =========================================================================
    # 4. Sales Orders
    # =========================================================================

    def _create_sales_orders(self, user, branch, currency, bookings, customers):
        self.stdout.write('\nCreating sales orders...')
        from modules.sales.models.order import SalesOrder, SalesOrderLine
        from modules.products.models import ProductTemplate, Uom

        products = list(ProductTemplate.objects.all()[:10])
        default_uom = Uom.objects.filter(name='Unit(s)').first() or Uom.objects.first()

        so_map = {'confirmed': 'sale', 'booked': 'sale', 'completed': 'done', 'in_process': 'sent'}
        created = []

        for booking in bookings:
            if booking.state in ['draft', 'cancelled']:
                continue

            so_state = so_map.get(booking.state, 'draft')
            order = SalesOrder.objects.create(
                partner=booking.partner,
                date_order=timezone.now() - timedelta(days=random.randint(1, 30)),
                validity_date=date.today() + timedelta(days=60),
                state='draft', user_id=user, currency_id=currency,
                client_order_ref=f'YALLA-{booking.name}',
                note=f'Tour booking: {booking.destination}',
            )

            revenue = booking.total_revenue or Decimal('1000')
            product = random.choice(products) if products else None
            SalesOrderLine.objects.create(
                order_id=order, sequence=1, product=product,
                name=f'Tour Package - {booking.destination} ({booking.duration_days}d)',
                product_uom_qty=Decimal('1'), product_uom=default_uom,
                price_unit=revenue, discount=Decimal('0'),
            )

            if booking.adults_count > 2 and products:
                SalesOrderLine.objects.create(
                    order_id=order, sequence=2, product=random.choice(products),
                    name='Extra passenger supplement',
                    product_uom_qty=Decimal(str(booking.adults_count - 2)),
                    product_uom=default_uom, price_unit=revenue * Decimal('0.3'),
                    discount=Decimal('0'),
                )

            order._compute_amounts()
            if so_state != 'draft':
                order.state = so_state
                order.save(update_fields=['state'])

            order.tour_booking = booking
            order.save(update_fields=['tour_booking'])
            created.append(order)

        self.stdout.write(f'  Sales orders: {len(created)}')
        return created

    # =========================================================================
    # 5. Purchase Orders
    # =========================================================================

    def _create_purchase_orders(self, user, branch, bookings, hotels_by_dest,
                                airlines, transport_suppliers):
        self.stdout.write('\nCreating purchase orders...')
        from modules.purchase.models import Order as PurchaseOrder, OrderLine
        from modules.products.models import ProductTemplate, Uom

        default_uom = Uom.objects.filter(name='Unit(s)').first() or Uom.objects.first()
        products = list(ProductTemplate.objects.all()[:5])
        po_states = ['draft', 'purchase', 'purchase', 'done']
        created = []

        for booking in bookings:
            if booking.state in ['draft', 'cancelled']:
                continue

            # PO for hotel
            hb = booking.hotels.first()
            if hb and hb.hotel:
                po = PurchaseOrder.objects.create(
                    partner=hb.hotel, user=user, branch=branch,
                    state=random.choice(po_states),
                    origin=f'YALLA-{booking.name}',
                    notes=f'Hotel for {booking.destination}',
                )
                cost = hb.cost_price or (hb.nightly_rate * Decimal('0.7') * (hb.nights_count or 1))
                OrderLine.objects.create(
                    order=po, sequence=1, product=products[0] if products else None,
                    name=f'Hotel: {hb.hotel.name} ({hb.nights_count or 0} nights)',
                    product_qty=Decimal('1'), product_uom=default_uom, price_unit=cost,
                )
                po._compute_amounts()
                po.tour_booking = booking
                po.save(update_fields=['tour_booking'])
                created.append(po)

            # PO for airline (50%)
            if random.random() < 0.5:
                flight = booking.flights.first()
                if flight and flight.airline:
                    po = PurchaseOrder.objects.create(
                        partner=flight.airline, user=user, branch=branch,
                        state=random.choice(po_states),
                        origin=f'YALLA-{booking.name}',
                        notes=f'Flights for {booking.destination}',
                    )
                    cost = (flight.adult_price or Decimal('500')) * Decimal('0.75') * booking.adults_count
                    OrderLine.objects.create(
                        order=po, sequence=1, product=products[1] if len(products) > 1 else None,
                        name=f'Flight: {flight.flight_number}',
                        product_qty=Decimal(str(booking.adults_count + booking.children_count)),
                        product_uom=default_uom,
                        price_unit=cost / max(1, booking.adults_count),
                    )
                    po._compute_amounts()
                    po.tour_booking = booking
                    po.save(update_fields=['tour_booking'])
                    created.append(po)

        self.stdout.write(f'  Purchase orders: {len(created)}')
        return created

    # =========================================================================
    # Summary
    # =========================================================================

    def _print_summary(self, destinations, hotels_by_dest, airlines,
                       transport_suppliers, package_types, packages,
                       bookings, sales_orders, purchase_orders):
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('YALLA THAILAND DEMO DATA SUMMARY'))
        self.stdout.write('=' * 60)

        total_hotels = sum(len(h) for h in hotels_by_dest.values())
        self.stdout.write(f'\nInfrastructure:')
        self.stdout.write(f'  Destinations: {len(destinations)}')
        self.stdout.write(f'  Hotels: {total_hotels}')
        self.stdout.write(f'  Airlines: {len(airlines)}')
        self.stdout.write(f'  Transport suppliers: {len(transport_suppliers)}')

        self.stdout.write(f'\nPackages:')
        self.stdout.write(f'  Package types: {len(package_types)}')
        self.stdout.write(f'  Tour packages (from CSV): {len(packages)}')

        # Show category breakdown
        cat_counts = {}
        for p in packages:
            cat = p.category_01 or 'Other'
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
        for cat, cnt in sorted(cat_counts.items()):
            self.stdout.write(f'    {cat}: {cnt}')

        self.stdout.write(f'\nBookings ({len(bookings)}):')
        state_counts = {}
        for b in bookings:
            state_counts[b.state] = state_counts.get(b.state, 0) + 1
        for s, c in state_counts.items():
            self.stdout.write(f'  {s}: {c}')

        total_rev = sum(b.total_revenue for b in bookings if b.total_revenue)
        total_cost = sum(b.total_cost for b in bookings if b.total_cost)
        self.stdout.write(f'\nFinancials:')
        self.stdout.write(f'  Revenue: {total_rev:,.2f}')
        self.stdout.write(f'  Cost: {total_cost:,.2f}')
        self.stdout.write(f'  Profit: {total_rev - total_cost:,.2f}')

        self.stdout.write(f'\nLinked Records:')
        self.stdout.write(f'  Sales orders: {len(sales_orders)}')
        self.stdout.write(f'  Purchase orders: {len(purchase_orders)}')
        self.stdout.write('=' * 60)


class _DryRunAbort(Exception):
    pass
