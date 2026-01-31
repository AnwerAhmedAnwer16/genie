# -*- coding: utf-8 -*-
"""Yalla Thailand UI views package"""

from .package_patches import (
    tourism_package_form_yalla_patch,
)

from .account_move_patches import (
    invoice_form_view_yalla_patch,
    vendor_bill_form_view_yalla_patch,
    journal_entry_form_view_yalla_patch,
    credit_note_form_view_yalla_patch,
    vendor_refund_form_view_yalla_patch,
)

from .sales_order_patches import (
    salesorder_form_view_yalla_patch,
    sales_quote_form_view_yalla_patch,
)

from .purchase_order_patches import (
    purchase_order_form_view_yalla_patch,
    purchase_ready_order_form_view_yalla_patch,
)

__all__ = [
    # Tourism package patches
    'tourism_package_form_yalla_patch',

    # Account move patches
    'invoice_form_view_yalla_patch',
    'vendor_bill_form_view_yalla_patch',
    'journal_entry_form_view_yalla_patch',
    'credit_note_form_view_yalla_patch',
    'vendor_refund_form_view_yalla_patch',

    # Sales order patches
    'salesorder_form_view_yalla_patch',
    'sales_quote_form_view_yalla_patch',

    # Purchase order patches
    'purchase_order_form_view_yalla_patch',
    'purchase_ready_order_form_view_yalla_patch',
]
