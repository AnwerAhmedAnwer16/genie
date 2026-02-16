# -*- coding: utf-8 -*-
"""
Awtar - Tour Package View Patches
Adds cost_per_person field to package form and list views.
"""
from django.utils.translation import gettext as _


# =============================================================================
# 1. PACKAGE FORM VIEW PATCH
# =============================================================================
tourism_package_form_awtar_patch = {
    "key": "tourism_package_form_awtar_patch",
    "name": "Tour Package Form - Awtar Patch",
    "model": "tourism.tourpackage",
    "view_type": "form",
    "priority": 21,
    "inherit_mode": "extension",
    "inherit_id": "tourism_package_form",
    "module": "tourism",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [
                {
                    "name": "cost_per_person",
                    "widget": "number",
                    "string": _("Cost Per Person"),
                    "readonly": True
                }
            ]
        }
    ]
}


# =============================================================================
# 2. PACKAGE LIST VIEW PATCH
# =============================================================================
tourism_package_list_awtar_patch = {
    "key": "tourism_package_list_awtar_patch",
    "name": "Tour Package List - Awtar Patch",
    "model": "tourism.tourpackage",
    "view_type": "list",
    "priority": 21,
    "inherit_mode": "extension",
    "inherit_id": "tourism_package_list",
    "module": "tourism",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "tree.fields",
            "content": [
                {
                    "name": "cost_per_person",
                    "widget": "number",
                    "string": _("Cost Per Person"),
                    "width": 120
                }
            ]
        }
    ]
}
