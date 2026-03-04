# -*- coding: utf-8 -*-
"""
Yalla Thailand Extensions - Extend existing models with custom fields.

1. TourPackage: Add 6 attachment fields (audio/video/pics in AR and EN)
2. AccountMove: Add package_type FK
3. SalesOrder: Add package_type FK
4. PurchaseOrder: Add package_type FK
"""
from modules.base.model_inheritance import ModelExtension
from modules.base.fields import AttachmentManyToManyField
from modules.base.decorators import action
from django.db import models, transaction
from django.utils.translation import gettext as _
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


class TourPackageYallaExtension(ModelExtension):
    """
    Extend TourPackage with Yalla Thailand trip fields matching final.csv columns.
    Select fields mirror the sheet columns exactly.
    """
    _inherit = 'tourism.tourpackage'
    _depends = ['tourism']

    # --- Choices ---
    DESTINATION_CHOICES = [
        ('phi_phi', 'Phi Phi'),
        ('james_bond', 'James Bond'),
        ('krabi_from_phuket', 'Krabi from Phuket'),
        ('krabi_from_krabi', 'Krabi from Krabi'),
        ('phang_nga', 'Phang Nga'),
        ('phuket', 'Phuket'),
        ('raya_coral', 'Raya & Coral'),
        ('similan', 'Similan'),
        ('bangkok', 'Bangkok'),
        ('koh_samui', 'Koh Samui'),
    ]

    MOTION_SICKNESS_CHOICES = [
        ('none', 'None'),
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    WEATHER_SENSITIVITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    CHILDREN_ELIGIBILITY_CHOICES = [
        ('1+', '1+'),
        ('3+', '3+'),
        ('8+', '8+'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('conditional', 'Conditional'),
    ]

    ACTION_ADRENALINE_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    ROMANTIC_HONEYMOON_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    SMOKER_FRIENDLY_CHOICES = [
        ('allowed', 'Allowed'),
        ('conditional', 'Conditional'),
    ]

    PRICE_RANGE_CHOICES = [
        ('<2000', '<2000 THB'),
        ('2000-3500', '2000-3500 THB'),
        ('>3500', '>3500 THB'),
    ]

    LUNCH_CHOICES = [
        ('none', 'None'),
        ('island', 'Island'),
        ('onboard', 'Onbaord'),
        ('restaurant', 'Rest.'),
        ('extra', 'Extra'),
    ]

    STOP_ACTIVITY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('9+', '9+'),
        ('custom', 'Custom'),
    ]

    DURATION_CHOICES = [
        ('3_hours', '3 Hours'),
        ('half_day', 'Half Day'),
        ('full_day', 'Full Day'),
        ('custom', 'Custom'),
    ]

    TIME_CHOICES = [
        ('early_morning', 'Early Morning'),
        ('early_bird', 'Early Bird'),
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('flexible', 'Flexible'),
        ('overnight', 'Overnight'),
    ]

    ACTIVITY_TYPE_CHOICES = [
        ('sea_trip', 'Sea Trip'),
        ('sea_adventure', 'Sea Adventure'),
        ('water_activity', 'Water Activity'),
        ('river_adventure', 'River Adventure'),
        ('land_adventure', 'Land Adventure'),
        ('evening_show', 'Evening Show'),
        ('city_tour', 'City Tour'),
    ]

    QUALITY_CHOICES = [
        ('economy', 'Economy'),
        ('average', 'Average'),
        ('conditional', 'Conditional'),
        ('premium', 'Premium'),
        ('high_end', 'High End'),
        ('luxury', 'Luxury'),
        ('private', 'Private'),
    ]

    SERVICE_ONBOARD_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    STABILITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    MOBILITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    BOAT_VIEW_CHOICES = [
        ('no_view', 'No View'),
        ('partial', 'Partial'),
        ('wide', 'Wide'),
        ('panoramic', 'Panoramic'),
    ]

    WATER_ACTIVITY_CHOICES = [
        ('none', 'None'),
        ('basic', 'Basic'),
        ('extra', 'Extra'),
        ('multiple', 'Multiple'),
    ]

    NO_OF_PAX_CHOICES = [
        ('<30', '<30'),
        ('30-60', '30-60'),
        ('>60', '>60'),
    ]

    LONGTAIL_BOAT_CHOICES = [
        ('none', 'None'),
        ('excluded', 'Excluded'),
        ('included', 'Included'),
        ('zodiac', 'Zodiac'),
    ]

    NATIONAL_PARK_CHOICES = [
        ('extra_200', 'Extra 200'),
        ('extra_300', 'Extra 300'),
        ('extra_400', 'Extra 400'),
        ('extra_500', 'Extra 500'),
        ('extra_600', 'Extra 600'),
        ('included', 'Included'),
    ]

    # --- Select fields matching final.csv columns ---
    destination = models.CharField(
        _("Destination"),
        max_length=50,
        choices=DESTINATION_CHOICES,
        null=True,
        blank=True,
    )
    motion_sickness = models.CharField(
        _("Motion Sickness"),
        max_length=20,
        choices=MOTION_SICKNESS_CHOICES,
        null=True,
        blank=True,
    )
    weather_sensitivity = models.CharField(
        _("Weather Sensitivity"),
        max_length=20,
        choices=WEATHER_SENSITIVITY_CHOICES,
        null=True,
        blank=True,
    )
    children_eligibility = models.CharField(
        _("Children Eligibility"),
        max_length=20,
        choices=CHILDREN_ELIGIBILITY_CHOICES,
        null=True,
        blank=True,
    )
    action_adrenaline = models.CharField(
        _("Action Adrenaline"),
        max_length=20,
        choices=ACTION_ADRENALINE_CHOICES,
        null=True,
        blank=True,
    )
    romantic_honeymoon = models.CharField(
        _("Romantic / Honeymoon"),
        max_length=20,
        choices=ROMANTIC_HONEYMOON_CHOICES,
        null=True,
        blank=True,
    )
    smoker_friendly = models.CharField(
        _("Smoker Friendly"),
        max_length=20,
        choices=SMOKER_FRIENDLY_CHOICES,
        null=True,
        blank=True,
    )
    price_range = models.CharField(
        _("Price Range"),
        max_length=20,
        choices=PRICE_RANGE_CHOICES,
        null=True,
        blank=True,
    )
    lunch = models.CharField(
        _("Lunch"),
        max_length=20,
        choices=LUNCH_CHOICES,
        null=True,
        blank=True,
    )
    stop_activity = models.CharField(
        _("Stop/Activity"),
        max_length=10,
        choices=STOP_ACTIVITY_CHOICES,
        null=True,
        blank=True,
    )
    duration = models.CharField(
        _("Duration"),
        max_length=20,
        choices=DURATION_CHOICES,
        null=True,
        blank=True,
    )
    time = models.CharField(
        _("Time"),
        max_length=20,
        choices=TIME_CHOICES,
        null=True,
        blank=True,
    )
    activity_type = models.CharField(
        _("Activity Type"),
        max_length=20,
        choices=ACTIVITY_TYPE_CHOICES,
        null=True,
        blank=True,
    )
    quality = models.CharField(
        _("Quality"),
        max_length=20,
        choices=QUALITY_CHOICES,
        null=True,
        blank=True,
    )
    service_onboard = models.CharField(
        _("Service Onboard"),
        max_length=20,
        choices=SERVICE_ONBOARD_CHOICES,
        null=True,
        blank=True,
    )
    stability = models.CharField(
        _("Stability"),
        max_length=20,
        choices=STABILITY_CHOICES,
        null=True,
        blank=True,
    )
    mobility = models.CharField(
        _("Mobility"),
        max_length=20,
        choices=MOBILITY_CHOICES,
        null=True,
        blank=True,
    )
    boat_view = models.CharField(
        _("Boat View"),
        max_length=20,
        choices=BOAT_VIEW_CHOICES,
        null=True,
        blank=True,
    )
    water_activity = models.CharField(
        _("Water Activity"),
        max_length=20,
        choices=WATER_ACTIVITY_CHOICES,
        null=True,
        blank=True,
    )
    no_of_pax = models.CharField(
        _("No. of PAX"),
        max_length=10,
        choices=NO_OF_PAX_CHOICES,
        null=True,
        blank=True,
    )
    longtail_boat = models.CharField(
        _("Longtail Boat"),
        max_length=20,
        choices=LONGTAIL_BOAT_CHOICES,
        null=True,
        blank=True,
    )
    national_park = models.CharField(
        _("National Park"),
        max_length=20,
        choices=NATIONAL_PARK_CHOICES,
        null=True,
        blank=True,
    )

    # --- Pricing ---
    sell_prc_adult = models.DecimalField(
        _("Sell PRC Ad."),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    net_prc_adult = models.DecimalField(
        _("Net PRC Ad."),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    sell_prc_child = models.DecimalField(
        _("Sell PRC Ch."),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    net_prc_child = models.DecimalField(
        _("Net PRC Ch."),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    min_markup = models.DecimalField(
        _("Min. Markup"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # --- Supplier ---
    supplier = models.ForeignKey(
        'base.Partner',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='yalla_supplied_packages',
        verbose_name=_("Supplier"),
    )

    # --- Media links ---
    whatsapp_catalog_link = models.URLField(
        _("WhatsApp Catalog Link"),
        max_length=500,
        null=True,
        blank=True,
    )
    video_link = models.URLField(
        _("Video Link"),
        max_length=500,
        null=True,
        blank=True,
    )
    album = models.CharField(
        _("Album"),
        max_length=255,
        null=True,
        blank=True,
    )
    note = models.TextField(
        _("Note"),
        null=True,
        blank=True,
    )

    # --- Attachment fields (AR/EN) ---
    audio_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/audio_ar',
        allowed_types=['audio'],
        blank=True,
        related_name='tourpackage_audio_ar',
        related_query_name='tourpackage_audio_ar',
        verbose_name=_("Audio (AR)"),
    )
    audio_en = AttachmentManyToManyField(
        upload_to='tourism/packages/audio_en',
        allowed_types=['audio'],
        blank=True,
        related_name='tourpackage_audio_en',
        related_query_name='tourpackage_audio_en',
        verbose_name=_("Audio (EN)"),
    )
    video_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/video_ar',
        allowed_types=['video'],
        blank=True,
        related_name='tourpackage_video_ar',
        related_query_name='tourpackage_video_ar',
        verbose_name=_("Video (AR)"),
    )
    video_en = AttachmentManyToManyField(
        upload_to='tourism/packages/video_en',
        allowed_types=['video'],
        blank=True,
        related_name='tourpackage_video_en',
        related_query_name='tourpackage_video_en',
        verbose_name=_("Video (EN)"),
    )
    pics_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/pics_ar',
        allowed_types=['image'],
        blank=True,
        related_name='tourpackage_pics_ar',
        related_query_name='tourpackage_pics_ar',
        verbose_name=_("Pictures (AR)"),
    )
    pics_en = AttachmentManyToManyField(
        upload_to='tourism/packages/pics_en',
        allowed_types=['image'],
        blank=True,
        related_name='tourpackage_pics_en',
        related_query_name='tourpackage_pics_en',
        verbose_name=_("Pictures (EN)"),
    )


class AccountMoveYallaExtension(ModelExtension):
    """
    Extend Account Move with package_type FK and client-paid-supplier action.
    """
    _inherit = 'account.move'
    _depends = ['account', 'tourism']

    package_type = models.ForeignKey(
        'tourism.PackageType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='account_moves',
        verbose_name=_("Package Type"),
        help_text=_("Tourism package type associated with this move")
    )

    related_bill = models.ForeignKey(
        'account.Move',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='yalla_linked_invoices',
        verbose_name=_("Related Supplier Bill"),
        help_text=_("Vendor bill that the client paid directly to the supplier")
    )

    @action
    def action_client_paid_supplier(self):
        """
        Client paid the supplier directly. Create a bridging journal entry
        that closes both the customer invoice (receivable) and vendor bill (payable).
        """
        from modules.account.models import Move, MoveLine, AccountSettings
        from modules.account.services.reconciliation import ReconciliationService

        moves = self if hasattr(self, '__iter__') else [self]
        for invoice in moves:
            # --- Validations ---
            if invoice.state != 'posted':
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('Invoice must be posted first.'), 'data': {}
                }
            if not invoice.related_bill:
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('Please set a Related Supplier Bill first.'), 'data': {}
                }
            bill = invoice.related_bill
            if bill.state != 'posted':
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('The related supplier bill must be posted.'), 'data': {}
                }
            if invoice.payment_state == 'paid':
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('This invoice is already paid.'), 'data': {}
                }

            amount = invoice.amount_total

            # --- Get accounts ---
            try:
                settings = AccountSettings.objects.filter(
                    company=invoice.company
                ).first()
            except Exception:
                settings = None

            # Receivable account: from invoice's receivable line or default
            inv_receivable_line = invoice.line_ids.filter(
                account__account_type='asset_receivable'
            ).first()
            if inv_receivable_line:
                receivable_account = inv_receivable_line.account
            elif settings and settings.default_receivable_account:
                receivable_account = settings.default_receivable_account
            else:
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('No receivable account found.'), 'data': {}
                }

            # Payable account: from bill's payable line or default
            bill_payable_line = bill.line_ids.filter(
                account__account_type='liability_payable'
            ).first()
            if bill_payable_line:
                payable_account = bill_payable_line.account
            elif settings and settings.default_payable_account:
                payable_account = settings.default_payable_account
            else:
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('No payable account found.'), 'data': {}
                }

            # Misc journal
            misc_journal = None
            if settings and settings.default_misc_journal:
                misc_journal = settings.default_misc_journal
            if not misc_journal:
                from modules.account.models import Journal
                misc_journal = Journal.objects.filter(
                    type='general'
                ).first()
            if not misc_journal:
                return {
                    'status': False, 'open_mode': 'message',
                    'message': _('No miscellaneous journal configured.'), 'data': {}
                }

            # --- Create bridging journal entry ---
            with transaction.atomic():
                from modules.base.models import Branch
                branch = getattr(invoice, 'branch', None)
                if not branch:
                    branch = Branch.objects.first()

                from django.utils import timezone
                je = Move.objects.create(
                    name='',
                    date=timezone.now().date(),
                    journal=misc_journal,
                    move_type='entry',
                    currency=invoice.currency,
                    branch=branch,
                    ref=_('Client Paid Supplier: %(inv)s ↔ %(bill)s') % {
                        'inv': invoice.name, 'bill': bill.name
                    },
                )

                # DR Payable (partner = supplier from bill)
                je_debit_line = MoveLine.objects.create(
                    move=je,
                    name=_('Client paid supplier – %(bill)s') % {'bill': bill.name},
                    account=payable_account,
                    partner=bill.partner,
                    debit=amount,
                    credit=Decimal('0.00'),
                    date=je.date,
                    currency=invoice.currency,
                )

                # CR Receivable (partner = client from invoice)
                je_credit_line = MoveLine.objects.create(
                    move=je,
                    name=_('Client paid supplier – %(inv)s') % {'inv': invoice.name},
                    account=receivable_account,
                    partner=invoice.partner,
                    debit=Decimal('0.00'),
                    credit=amount,
                    date=je.date,
                    currency=invoice.currency,
                )

                # Post the JE
                if not je.name:
                    je.name = je._generate_name()
                je.state = 'posted'
                je.posted_before = True
                je.save()

                # --- Reconcile receivable: JE credit ↔ invoice's receivable debit ---
                if inv_receivable_line:
                    ReconciliationService.reconcile([inv_receivable_line, je_credit_line])

                # --- Reconcile payable: JE debit ↔ bill's payable credit ---
                if bill_payable_line:
                    ReconciliationService.reconcile([bill_payable_line, je_debit_line])

                # --- Update residual & payment_state on invoice ---
                inv_new_residual = max(invoice.amount_residual - amount, Decimal('0.00'))
                inv_ps = 'paid' if inv_new_residual <= 0 else 'partial'
                Move.objects.filter(pk=invoice.pk).update(
                    amount_residual=inv_new_residual,
                    payment_state=inv_ps,
                )

                # --- Update residual & payment_state on bill ---
                bill_new_residual = max(bill.amount_residual - amount, Decimal('0.00'))
                bill_ps = 'paid' if bill_new_residual <= 0 else 'partial'
                Move.objects.filter(pk=bill.pk).update(
                    amount_residual=bill_new_residual,
                    payment_state=bill_ps,
                )

            return {
                'status': True,
                'open_mode': 'message',
                'message': _(
                    'Done! Journal entry %(je)s created. '
                    'Invoice → %(inv_state)s, Bill → %(bill_state)s.'
                ) % {
                    'je': je.name,
                    'inv_state': inv_ps,
                    'bill_state': bill_ps,
                },
                'on_success': {'type': 'refresh'}

            }


class PartnerYallaExtension(ModelExtension):
    """
    Extend Partner with supplier settlement action.
    """
    _inherit = 'base.partner'
    _depends = ['base', 'account']

    @action
    def action_supplier_settlement(self):
        """
        Check unreconciled payable balance for this supplier
        and open a pre-filled payment form to settle the net difference.
        """
        from modules.account.models import MoveLine

        partners = self if hasattr(self, '__iter__') else [self]
        for partner in partners:
            # Query all unreconciled lines on payable accounts for this partner
            payable_lines = MoveLine.objects.filter(
                partner=partner,
                account__account_type='liability_payable',
                move__state='posted',
                reconciled=False,
            )

            total_debit = payable_lines.aggregate(
                total=models.Sum('debit')
            )['total'] or Decimal('0.00')
            total_credit = payable_lines.aggregate(
                total=models.Sum('credit')
            )['total'] or Decimal('0.00')

            net = total_debit - total_credit

            if abs(net) < Decimal('0.01'):
                return {
                    'status': True, 'open_mode': 'message',
                    'message': _('Account is already settled for %(name)s.') % {
                        'name': partner.name
                    },
                    'data': {}
                }

            if net > 0:
                # Supplier owes us → inbound payment
                payment_type = 'inbound'
                menu_key = 'account_customer_payments'
                abs_amount = float(net)
            else:
                # We owe supplier → outbound payment
                payment_type = 'outbound'
                menu_key = 'account_vendor_payments'
                abs_amount = float(abs(net))

            return {
                'status': True,
                'open_mode': 'slideover',
                'data': {
                    'menu_item_key': menu_key,
                    'view_type': 'form',
                    'context': {
                        'default_fields': {
                            'partner': partner,
                            'amount': abs_amount,
                            'payment_type': payment_type,
                        }
                    },
                    'type': 'action',
                    'title': _('Settle Account – %(name)s') % {'name': partner.name}
                }
            }


class SalesOrderYallaExtension(ModelExtension):
    """
    Extend Sales Order with package_type FK.
    """
    _inherit = 'sales.salesorder'
    _depends = ['sales', 'tourism']

    package_type = models.ForeignKey(
        'tourism.PackageType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sales_orders',
        verbose_name=_("Package Type"),
        help_text=_("Tourism package type associated with this sales order")
    )


class PurchaseOrderYallaExtension(ModelExtension):
    """
    Extend Purchase Order with package_type FK.
    """
    _inherit = 'purchase.order'
    _depends = ['purchase', 'tourism']

    package_type = models.ForeignKey(
        'tourism.PackageType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='purchase_orders_package_type',
        verbose_name=_("Package Type"),
        help_text=_("Tourism package type associated with this purchase order")
    )
