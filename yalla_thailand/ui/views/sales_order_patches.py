# -*- coding: utf-8 -*-
"""
Yalla Thailand - Sales Order Form View Patches
Adds package_type FK field to both sales order form views.
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
# 1. SALES ORDER FORM VIEW PATCH
# =============================================================================
salesorder_form_view_yalla_patch = {
    "key": "salesorder_form_view_yalla_patch",
    "name": "Sales Order Form - Yalla Thailand Patch",
    "model": "sales.salesorder",
    "view_type": "form",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "salesorder_form_view",
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
# 2. SALES QUOTATION FORM VIEW PATCH
# =============================================================================
sales_quote_form_view_yalla_patch = {
    "key": "sales_quote_form_view_yalla_patch",
    "name": "Sales Quotation Form - Yalla Thailand Patch",
    "model": "sales.salesorder",
    "view_type": "form",
    "priority": 21,
    "inherit_mode": "extension",
    "inherit_id": "sales_quote_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [_package_type_field]
        }
    ]
}
