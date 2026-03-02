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
from django.db import models
from django.utils.translation import gettext as _


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

    STOP_ACT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
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
    ]

    ACT_TYPE_CHOICES = [
        ('sea_trip', 'Sea Trip'),
        ('sea_adventure', 'Sea Adventure'),
        ('water_activity', 'Water Activity'),
        ('river_adventure', 'River Adventure'),
        ('land_adventure', 'Land Adventure'),
        ('evening_show', 'Evening Show'),
    ]

    QUALITY_CHOICES = [
        ('economy', 'Economy'),
        ('average', 'Average'),
        ('conditional', 'Conditional'),
        ('premium', 'Premium'),
        ('high_end', 'High End'),
        ('luxury', 'Luxury'),
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

    WATER_ACT_CHOICES = [
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
        ('extra_300', 'Extra 300'),
        ('extra_400', 'Extra 400'),
    ]

    # --- Select fields matching final.csv columns ---
    destination = models.CharField(
        _("Destination"),
        max_length=50,
        choices=DESTINATION_CHOICES,
        blank=True,
    )
    motion_sickness = models.CharField(
        _("Motion Sickness"),
        max_length=20,
        choices=MOTION_SICKNESS_CHOICES,
        blank=True,
    )
    weather_sensitivity = models.CharField(
        _("Weather Sensitivity"),
        max_length=20,
        choices=WEATHER_SENSITIVITY_CHOICES,
        blank=True,
    )
    children_eligibility = models.CharField(
        _("Children Eligibility"),
        max_length=20,
        choices=CHILDREN_ELIGIBILITY_CHOICES,
        blank=True,
    )
    action_adrenaline = models.CharField(
        _("Action Adrenaline"),
        max_length=20,
        choices=ACTION_ADRENALINE_CHOICES,
        blank=True,
    )
    romantic_honeymoon = models.CharField(
        _("Romantic / Honeymoon"),
        max_length=20,
        choices=ROMANTIC_HONEYMOON_CHOICES,
        blank=True,
    )
    smoker_friendly = models.CharField(
        _("Smoker Friendly"),
        max_length=20,
        choices=SMOKER_FRIENDLY_CHOICES,
        blank=True,
    )
    price_range = models.CharField(
        _("Price Range"),
        max_length=20,
        choices=PRICE_RANGE_CHOICES,
        blank=True,
    )
    lunch = models.CharField(
        _("Lunch"),
        max_length=20,
        choices=LUNCH_CHOICES,
        blank=True,
    )
    stop_act = models.CharField(
        _("Stop/Act."),
        max_length=10,
        choices=STOP_ACT_CHOICES,
        blank=True,
    )
    duration = models.CharField(
        _("Duration"),
        max_length=20,
        choices=DURATION_CHOICES,
        blank=True,
    )
    time = models.CharField(
        _("Time"),
        max_length=20,
        choices=TIME_CHOICES,
        blank=True,
    )
    act_type = models.CharField(
        _("Act. Type"),
        max_length=20,
        choices=ACT_TYPE_CHOICES,
        blank=True,
    )
    quality = models.CharField(
        _("Quality"),
        max_length=20,
        choices=QUALITY_CHOICES,
        blank=True,
    )
    service_onboard = models.CharField(
        _("Service Onboard"),
        max_length=20,
        choices=SERVICE_ONBOARD_CHOICES,
        blank=True,
    )
    stability = models.CharField(
        _("Stability"),
        max_length=20,
        choices=STABILITY_CHOICES,
        blank=True,
    )
    mobility = models.CharField(
        _("Mobility"),
        max_length=20,
        choices=MOBILITY_CHOICES,
        blank=True,
    )
    boat_view = models.CharField(
        _("Boat View"),
        max_length=20,
        choices=BOAT_VIEW_CHOICES,
        blank=True,
    )
    water_act = models.CharField(
        _("Water Act."),
        max_length=20,
        choices=WATER_ACT_CHOICES,
        blank=True,
    )
    no_of_pax = models.CharField(
        _("No. of PAX"),
        max_length=10,
        choices=NO_OF_PAX_CHOICES,
        blank=True,
    )
    longtail_boat = models.CharField(
        _("Longtail Boat"),
        max_length=20,
        choices=LONGTAIL_BOAT_CHOICES,
        blank=True,
    )
    national_park = models.CharField(
        _("National Park"),
        max_length=20,
        choices=NATIONAL_PARK_CHOICES,
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
        blank=True,
    )
    video_link = models.URLField(
        _("Video Link"),
        max_length=500,
        blank=True,
    )
    album = models.CharField(
        _("Album"),
        max_length=255,
        blank=True,
    )
    note = models.TextField(
        _("Note"),
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
    Extend Account Move with package_type FK.
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
