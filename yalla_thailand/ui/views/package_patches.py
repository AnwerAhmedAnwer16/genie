# -*- coding: utf-8 -*-
"""
Yalla Thailand - Tour Package View Patches
Adds Yalla-specific fields (trip categories, pricing, supplier, tags, media)
to the TourPackage form, list, and search views.
"""
from django.utils.translation import gettext as _


# =============================================================================
# FORM VIEW PATCH
# =============================================================================
tourism_package_form_yalla_patch = {
    "key": "tourism_package_form_yalla_patch",
    "name": "Tour Package Form - Yalla Thailand Patch",
    "model": "tourism.tourpackage",
    "view_type": "form",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "tourism_package_form",
    "module": "yalla_thailand",
    "inheritance_operations": [
        # 1. Add categories + supplier + duration_type to main section (left group)
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.0.fields",
            "content": [
                {
                    "name": "category_01",
                    "widget": "text",
                    "string": _("Category 1"),
                },
                {
                    "name": "category_02",
                    "widget": "text",
                    "string": _("Category 2"),
                },
                {
                    "name": "category_03",
                    "widget": "text",
                    "string": _("Category 3"),
                },
                {
                    "name": "duration_type",
                    "widget": "text",
                    "string": _("Duration Type"),
                    "help": _("e.g., Full Day, Half Day, Evening"),
                },
            ]
        },
        # 2. Add pricing + supplier to main section (right group)
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [
                {
                    "name": "min_selling_price",
                    "widget": "number",
                    "string": _("Min Selling Price"),
                },
                {
                    "name": "net_price",
                    "widget": "number",
                    "string": _("Net Price"),
                },
                {
                    "name": "supplier",
                    "widget": "relation",
                    "string": _("Supplier"),
                    "displayField": "name",
                    "multiSelect": False,
                },
            ]
        },
        # 3. Replace Attachments tab (index 4) with tags + media + attachments
        {
            "operation": "replace",
            "target": "sheet.tabs.4",
            "content": {
                "title": _("Tags & Media"),
                "sections": [
                    {
                        "title": _("Trip Tags"),
                        "groups": [
                            {
                                "fields": [
                                    {
                                        "name": "kids_friendly",
                                        "widget": "switch",
                                        "string": _("Kids Friendly"),
                                    },
                                    {
                                        "name": "action_adrenaline",
                                        "widget": "switch",
                                        "string": _("Action / Adrenaline"),
                                    },
                                    {
                                        "name": "family_friendly",
                                        "widget": "switch",
                                        "string": _("Family Friendly"),
                                    },
                                ],
                            },
                            {
                                "fields": [
                                    {
                                        "name": "romantic_honeymoon",
                                        "widget": "switch",
                                        "string": _("Romantic / Honeymoon"),
                                    },
                                    {
                                        "name": "smoker_friendly",
                                        "widget": "switch",
                                        "string": _("Smoker Friendly"),
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "title": _("Media Links"),
                        "groups": [
                            {
                                "fields": [
                                    {
                                        "name": "whatsapp_catalog_link",
                                        "widget": "url",
                                        "string": _("WhatsApp Catalog Link"),
                                    },
                                    {
                                        "name": "video_link",
                                        "widget": "url",
                                        "string": _("Video Link"),
                                    },
                                    {
                                        "name": "album",
                                        "widget": "text",
                                        "string": _("Album"),
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "title": _("Attachments"),
                        "groups": [
                            {
                                "fullWidth": True,
                                "fields": [
                                    {
                                        "name": "audio_ar",
                                        "widget": "files",
                                        "string": _("Audio (AR)"),
                                        "accept": "audio/*",
                                    },
                                    {
                                        "name": "audio_en",
                                        "widget": "files",
                                        "string": _("Audio (EN)"),
                                        "accept": "audio/*",
                                    },
                                    {
                                        "name": "video_ar",
                                        "widget": "files",
                                        "string": _("Video (AR)"),
                                        "accept": "video/*",
                                    },
                                    {
                                        "name": "video_en",
                                        "widget": "files",
                                        "string": _("Video (EN)"),
                                        "accept": "video/*",
                                    },
                                    {
                                        "name": "pics_ar",
                                        "widget": "files",
                                        "string": _("Pictures (AR)"),
                                        "accept": "image/*",
                                    },
                                    {
                                        "name": "pics_en",
                                        "widget": "files",
                                        "string": _("Pictures (EN)"),
                                        "accept": "image/*",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        },
    ],
}


# =============================================================================
# LIST VIEW PATCH
# =============================================================================
tourism_package_list_yalla_patch = {
    "key": "tourism_package_list_yalla_patch",
    "name": "Tour Package List - Yalla Thailand Patch",
    "model": "tourism.tourpackage",
    "view_type": "list",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "tourism_package_list",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "tree.fields",
            "content": [
                {
                    "name": "category_01",
                    "widget": "text",
                    "string": _("Category"),
                    "width": 120,
                },
                {
                    "name": "supplier",
                    "widget": "relation",
                    "displayField": "name",
                    "string": _("Supplier"),
                    "width": 150,
                },
                {
                    "name": "min_selling_price",
                    "widget": "number",
                    "string": _("Min Selling"),
                    "width": 110,
                },
                {
                    "name": "net_price",
                    "widget": "number",
                    "string": _("Net Price"),
                    "width": 110,
                },
                {
                    "name": "duration_type",
                    "widget": "text",
                    "string": _("Duration Type"),
                    "width": 110,
                },
            ],
        },
    ],
}


# =============================================================================
# SEARCH VIEW PATCH
# =============================================================================
tourism_package_search_yalla_patch = {
    "key": "tourism_package_search_yalla_patch",
    "name": "Tour Package Search - Yalla Thailand Patch",
    "model": "tourism.tourpackage",
    "view_type": "search",
    "priority": 20,
    "inherit_mode": "extension",
    "inherit_id": "tourism_package_search",
    "module": "yalla_thailand",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "search.filters",
            "content": [
                {
                    "name": "kids_friendly",
                    "string": _("Kids Friendly"),
                    "filter": {
                        "field": "kids_friendly",
                        "operator": "eq",
                        "value": True,
                    },
                },
                {
                    "name": "family_friendly",
                    "string": _("Family Friendly"),
                    "filter": {
                        "field": "family_friendly",
                        "operator": "eq",
                        "value": True,
                    },
                },
                {
                    "name": "romantic_honeymoon",
                    "string": _("Romantic / Honeymoon"),
                    "filter": {
                        "field": "romantic_honeymoon",
                        "operator": "eq",
                        "value": True,
                    },
                },
                {
                    "name": "action_adrenaline",
                    "string": _("Action / Adrenaline"),
                    "filter": {
                        "field": "action_adrenaline",
                        "operator": "eq",
                        "value": True,
                    },
                },
            ],
        },
        {
            "operation": "append",
            "target": "search.group_by",
            "content": [
                {
                    "name": "category_01",
                    "string": _("Category 1"),
                },
                {
                    "name": "supplier",
                    "string": _("Supplier"),
                },
                {
                    "name": "duration_type",
                    "string": _("Duration Type"),
                },
            ],
        },
    ],
}
