# -*- coding: utf-8 -*-
"""
Yalla Thailand - Partner Form View Patch
Adds "Settle Account" action button to partner form.
"""
from django.utils.translation import gettext as _


partner_form_yalla_settle_patch = {
    "key": "partner_form_yalla_settle_patch",
    "name": "Partner Form - Yalla Thailand Settle Patch",
    "model": "base.partner",
    "view_type": "form",
    "priority": 300,
    "inherit_mode": "extension",
    "inherit_id": "base_partner_form_view",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "header.actions",
            "content": [
                {
                    "name": "action_supplier_settlement",
                    "type": "server",
                    'as': 'button',
                    "string": _("Settle Account"),
                    "icon": "Scale",
                }
            ]
        }
    ]
}
