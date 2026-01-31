# -*- coding: utf-8 -*-
"""
Yalla Thailand - Purchase Order Form View Patches
Adds package_type FK field to both purchase order form views.
"""
from django.utils.translation import gettext as _


_package_type_field = {
    "name": "package_type",
    "string": _("Package Type"),
    "widget": "relation",
    "displayField": "name",
    "multiSelect": False
}


# =============================================================================
# 1. PURCHASE RFQ FORM VIEW PATCH
# =============================================================================
purchase_order_form_view_yalla_patch = {
    "key": "purchase_order_form_view_yalla_patch",
    "name": "Purchase Order Form (RFQ) - Yalla Thailand Patch",
    "model": "purchase.order",
    "view_type": "form",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "purchase_order_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [_package_type_field]
        }
    ]
}


# =============================================================================
# 2. PURCHASE READY ORDER FORM VIEW PATCH
# =============================================================================
purchase_ready_order_form_view_yalla_patch = {
    "key": "purchase_ready_order_form_view_yalla_patch",
    "name": "Purchase Order Form (Ready) - Yalla Thailand Patch",
    "model": "purchase.order",
    "view_type": "form",
    "priority": 21,
    "inherit_mode": "extension",
    "inherit_id": "purchase_ready_order_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [_package_type_field]
        }
    ]
}
