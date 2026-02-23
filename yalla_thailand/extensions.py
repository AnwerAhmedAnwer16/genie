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
    Extend TourPackage with Yalla Thailand trip fields and attachment fields.
    Maps CSV columns that don't exist on TourPackage:
    - Category.01/02/03, Min Selling, Net PRC, Supplier, Duration type
    - Tags: Kids friendly, Action Adrenaline, Family Friendly, Romantic/Honeymoon, Smoker Friendly
    - Media: WhatsApp Catalog Link, Video, Album
    Already mapped to TourPackage: Trip Name→name, Short Description→description, Selling PRC→base_price
    """
    _inherit = 'tourism.tourpackage'
    _depends = ['tourism']

    # --- CSV trip categories ---
    category_01 = models.CharField(
        _("Category 1"),
        max_length=100,
        blank=True,
        help_text=_("Primary category (e.g., Phi Phi, James Bond, Krabi)")
    )
    category_02 = models.CharField(
        _("Category 2"),
        max_length=100,
        blank=True,
        help_text=_("Secondary category (e.g., Economy Trips, Luxury Trips)")
    )
    category_03 = models.CharField(
        _("Category 3"),
        max_length=100,
        blank=True,
        help_text=_("Tertiary category (optional)")
    )

    # --- CSV pricing ---
    min_selling_price = models.DecimalField(
        _("Min Selling Price"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Minimum selling price (THB)")
    )
    net_price = models.DecimalField(
        _("Net Price"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Net/cost price from supplier (THB)")
    )

    # --- CSV supplier ---
    supplier = models.ForeignKey(
        'base.Partner',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='yalla_supplied_packages',
        verbose_name=_("Supplier"),
        help_text=_("Trip supplier/operator")
    )

    # --- CSV duration type ---
    duration_type = models.CharField(
        _("Duration Type"),
        max_length=50,
        blank=True,
        help_text=_("Duration type (e.g., Full Day, Half Day, Evening)")
    )

    # --- CSV tags ---
    kids_friendly = models.BooleanField(
        _("Kids Friendly"),
        default=False,
        help_text=_("Suitable for children")
    )
    action_adrenaline = models.BooleanField(
        _("Action / Adrenaline"),
        default=False,
        help_text=_("Adventure/adrenaline activity")
    )
    family_friendly = models.BooleanField(
        _("Family Friendly"),
        default=False,
        help_text=_("Suitable for families")
    )
    romantic_honeymoon = models.BooleanField(
        _("Romantic / Honeymoon"),
        default=False,
        help_text=_("Suitable for couples/honeymoon")
    )
    smoker_friendly = models.BooleanField(
        _("Smoker Friendly"),
        default=False,
        help_text=_("Smoking allowed")
    )

    # --- CSV media links ---
    whatsapp_catalog_link = models.URLField(
        _("WhatsApp Catalog Link"),
        max_length=500,
        blank=True,
        help_text=_("WhatsApp product catalog link")
    )
    video_link = models.URLField(
        _("Video Link"),
        max_length=500,
        blank=True,
        help_text=_("Video URL for this trip")
    )
    album = models.CharField(
        _("Album"),
        max_length=255,
        blank=True,
        help_text=_("Album reference name")
    )

    # --- Attachment fields (AR/EN) ---
    audio_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/audio_ar',
        allowed_types=['audio'],
        blank=True,
        related_name='tourpackage_audio_ar',
        related_query_name='tourpackage_audio_ar',
        verbose_name=_("Audio (AR)"),
        help_text=_("Arabic audio files for this package")
    )

    audio_en = AttachmentManyToManyField(
        upload_to='tourism/packages/audio_en',
        allowed_types=['audio'],
        blank=True,
        related_name='tourpackage_audio_en',
        related_query_name='tourpackage_audio_en',
        verbose_name=_("Audio (EN)"),
        help_text=_("English audio files for this package")
    )

    video_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/video_ar',
        allowed_types=['video'],
        blank=True,
        related_name='tourpackage_video_ar',
        related_query_name='tourpackage_video_ar',
        verbose_name=_("Video (AR)"),
        help_text=_("Arabic video files for this package")
    )

    video_en = AttachmentManyToManyField(
        upload_to='tourism/packages/video_en',
        allowed_types=['video'],
        blank=True,
        related_name='tourpackage_video_en',
        related_query_name='tourpackage_video_en',
        verbose_name=_("Video (EN)"),
        help_text=_("English video files for this package")
    )

    pics_ar = AttachmentManyToManyField(
        upload_to='tourism/packages/pics_ar',
        allowed_types=['image'],
        blank=True,
        related_name='tourpackage_pics_ar',
        related_query_name='tourpackage_pics_ar',
        verbose_name=_("Pictures (AR)"),
        help_text=_("Arabic pictures for this package")
    )

    pics_en = AttachmentManyToManyField(
        upload_to='tourism/packages/pics_en',
        allowed_types=['image'],
        blank=True,
        related_name='tourpackage_pics_en',
        related_query_name='tourpackage_pics_en',
        verbose_name=_("Pictures (EN)"),
        help_text=_("English pictures for this package")
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
