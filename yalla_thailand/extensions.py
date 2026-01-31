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
    Extend TourPackage with separate attachment fields for Arabic and English content.
    Replaces the generic attachments field with 6 specific fields.
    """
    _inherit = 'tourism.tourpackage'
    _depends = ['tourism']

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
