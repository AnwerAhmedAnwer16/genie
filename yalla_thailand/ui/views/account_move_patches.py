# -*- coding: utf-8 -*-
"""
Yalla Thailand - Account Move Form View Patches
Adds package_type FK field to all 5 account.move form views.
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
# 1. INVOICE FORM VIEW PATCH
# =============================================================================
invoice_form_view_yalla_patch = {
    "key": "invoice_form_view_yalla_patch",
    "name": "Invoice Form - Yalla Thailand Patch",
    "model": "account.move",
    "view_type": "form",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "invoice_form_view",
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
# 2. VENDOR BILL FORM VIEW PATCH
# =============================================================================
vendor_bill_form_view_yalla_patch = {
    "key": "vendor_bill_form_view_yalla_patch",
    "name": "Vendor Bill Form - Yalla Thailand Patch",
    "model": "account.move",
    "view_type": "form",
    "priority": 21,
    "inherit_mode": "extension",
    "inherit_id": "vendor_bill_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.0.fields",
            "content": [_package_type_field]
        }
    ]
}


# =============================================================================
# 3. JOURNAL ENTRY FORM VIEW PATCH
# =============================================================================
journal_entry_form_view_yalla_patch = {
    "key": "journal_entry_form_view_yalla_patch",
    "name": "Journal Entry Form - Yalla Thailand Patch",
    "model": "account.move",
    "view_type": "form",
    "priority": 22,
    "inherit_mode": "extension",
    "inherit_id": "journal_entry_form_view",
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
# 4. CREDIT NOTE FORM VIEW PATCH
# =============================================================================
credit_note_form_view_yalla_patch = {
    "key": "credit_note_form_view_yalla_patch",
    "name": "Credit Note Form - Yalla Thailand Patch",
    "model": "account.move",
    "view_type": "form",
    "priority": 23,
    "inherit_mode": "extension",
    "inherit_id": "credit_note_form_view",
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
# 5. VENDOR REFUND FORM VIEW PATCH
# =============================================================================
vendor_refund_form_view_yalla_patch = {
    "key": "vendor_refund_form_view_yalla_patch",
    "name": "Vendor Refund Form - Yalla Thailand Patch",
    "model": "account.move",
    "view_type": "form",
    "priority": 24,
    "inherit_mode": "extension",
    "inherit_id": "vendor_refund_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.0.fields",
            "content": [_package_type_field]
        }
    ]
}
