# -*- coding: utf-8 -*-
"""
Awtar Extensions - Add cost_per_person to TourPackage.
Auto-computed on save: total PO amount / package seats.
"""
from decimal import Decimal
from modules.base.model_inheritance import ModelExtension
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _


class TourPackageAwtarExtension(ModelExtension):
    _inherit = 'tourism.tourpackage'
    _depends = ['tourism']

    cost_per_person = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00'),
        null=True,
        blank=True,
        verbose_name=_("Cost Per Person"),
        help_text=_("Cost per person = Total POs / seats")
    )

    def post_save(self):
        """Auto-compute cost_per_person from total POs / package_seats."""
        if self.pk and self.package_seats and self.package_seats > 0:
            from modules.purchase.models import Order
            result = Order.objects.filter(
                tour_package=self
            ).aggregate(total=Sum('amount_total'))
            total = result['total'] or Decimal('0.00')
            new_cost = total / self.package_seats
            if new_cost != (self.cost_per_person or Decimal('0.00')):
                type(self).objects.filter(pk=self.pk).update(cost_per_person=new_cost)
                self.cost_per_person = new_cost
