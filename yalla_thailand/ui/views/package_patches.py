# -*- coding: utf-8 -*-
"""
Yalla Thailand - Tour Package View Patches
Adds Yalla-specific select fields (matching final.csv columns)
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
        # 1. Trip Info fields (left group) - destination, categories, timing
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.0.fields",
            "content": [
                {
                    "name": "supplier",
                    "widget": "relation",
                    "string": _("Supplier"),
                    "displayField": "name",
                    "multiSelect": False,
                    "required": False,
                },
                {
                    "name": "destination",
                    "widget": "select",
                    "string": _("Destination"),
                    "required": False,
                },
                {
                    "name": "activity_type",
                    "widget": "select",
                    "string": _("Act. Type"),
                    "required": False,
                },
                {
                    "name": "duration",
                    "widget": "select",
                    "string": _("Duration"),
                    "required": False,
                },
                {
                    "name": "time",
                    "widget": "select",
                    "string": _("Time"),
                    "required": False,
                },
                {
                    "name": "stop_activity",
                    "widget": "select",
                    "string": _("Stop/Act."),
                    "required": False,
                },
            ]
        },
        # 2. Quality & Comfort fields (right group)
        {
            "operation": "append",
            "target": "sheet.sections.0.groups.1.fields",
            "content": [
                {
                    "name": "quality",
                    "widget": "select",
                    "string": _("Quality"),
                    "required": False,
                },
                {
                    "name": "price_range",
                    "widget": "select",
                    "string": _("Price Range"),
                    "required": False,
                },
                {
                    "name": "lunch",
                    "widget": "select",
                    "string": _("Lunch"),
                    "required": False,
                },
                {
                    "name": "longtail_boat",
                    "widget": "select",
                    "string": _("Longtail Boat"),
                    "required": False,
                },
                {
                    "name": "national_park",
                    "widget": "select",
                    "string": _("National Park"),
                    "required": False,
                },
                {
                    "name": "no_of_pax",
                    "widget": "select",
                    "string": _("No. of PAX"),
                    "required": False,
                },
            ]
        },
        # 3. Replace Tags & Media tab with all select fields + media + attachments
        {
            "operation": "replace",
            "target": "sheet.tabs.4",
            "content": {
                "title": _("Trip Details"),
                "sections": [
                    {
                        "title": _("Safety & Comfort"),
                        "groups": [
                            {
                                "fields": [
                                    {
                                        "name": "motion_sickness",
                                        "widget": "select",
                                        "string": _("Motion Sickness"),
                                        "required": False,
                                    },
                                    {
                                        "name": "weather_sensitivity",
                                        "widget": "select",
                                        "string": _("Weather Sensitivity"),
                                        "required": False,
                                    },
                                    {
                                        "name": "children_eligibility",
                                        "widget": "select",
                                        "string": _("Children Eligibility"),
                                        "required": False,
                                    },
                                    {
                                        "name": "stability",
                                        "widget": "select",
                                        "string": _("Stability"),
                                        "required": False,
                                    },
                                ],
                            },
                            {
                                "fields": [
                                    {
                                        "name": "action_adrenaline",
                                        "widget": "select",
                                        "string": _("Action Adrenaline"),
                                        "required": False,
                                    },
                                    {
                                        "name": "romantic_honeymoon",
                                        "widget": "select",
                                        "string": _("Romantic / Honeymoon"),
                                        "required": False,
                                    },
                                    {
                                        "name": "smoker_friendly",
                                        "widget": "select",
                                        "string": _("Smoker Friendly"),
                                        "required": False,
                                    },
                                    {
                                        "name": "mobility",
                                        "widget": "select",
                                        "string": _("Mobility"),
                                        "required": False,
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "title": _("Boat & Water"),
                        "groups": [
                            {
                                "fields": [
                                    {
                                        "name": "service_onboard",
                                        "widget": "select",
                                        "string": _("Service Onboard"),
                                        "required": False,
                                    },
                                    {
                                        "name": "boat_view",
                                        "widget": "select",
                                        "string": _("Boat View"),
                                        "required": False,
                                    },
                                    {
                                        "name": "water_activity",
                                        "widget": "select",
                                        "string": _("Water Act."),
                                        "required": False,
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        "title": _("Pricing"),
                        "groups": [
                            {
                                "fields": [
                                    {
                                        "name": "sell_prc_adult",
                                        "widget": "number",
                                        "string": _("Sell PRC Ad."),
                                        "required": False,
                                    },
                                    {
                                        "name": "net_prc_adult",
                                        "widget": "number",
                                        "string": _("Net PRC Ad."),
                                        "required": False,
                                    },
                                    {
                                        "name": "min_markup",
                                        "widget": "number",
                                        "string": _("Min. Markup"),
                                        "required": False,
                                    },
                                ],
                            },
                            {
                                "fields": [
                                    {
                                        "name": "sell_prc_child",
                                        "widget": "number",
                                        "string": _("Sell PRC Ch."),
                                        "required": False,
                                    },
                                    {
                                        "name": "net_prc_child",
                                        "widget": "number",
                                        "string": _("Net PRC Ch."),
                                        "required": False,
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
                                        "required": False,
                                    },
                                    {
                                        "name": "video_link",
                                        "widget": "url",
                                        "string": _("Video Link"),
                                        "required": False,
                                    },
                                    {
                                        "name": "album",
                                        "widget": "text",
                                        "string": _("Album"),
                                        "required": False,
                                    },
                                    {
                                        "name": "note",
                                        "widget": "text",
                                        "string": _("Note"),
                                        "required": False,
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
                                        "required": False,
                                    },
                                    {
                                        "name": "audio_en",
                                        "widget": "files",
                                        "string": _("Audio (EN)"),
                                        "accept": "audio/*",
                                        "required": False,
                                    },
                                    {
                                        "name": "video_ar",
                                        "widget": "files",
                                        "string": _("Video (AR)"),
                                        "accept": "video/*",
                                        "required": False,
                                    },
                                    {
                                        "name": "video_en",
                                        "widget": "files",
                                        "string": _("Video (EN)"),
                                        "accept": "video/*",
                                        "required": False,
                                    },
                                    {
                                        "name": "pics_ar",
                                        "widget": "files",
                                        "string": _("Pictures (AR)"),
                                        "accept": "image/*",
                                        "required": False,
                                    },
                                    {
                                        "name": "pics_en",
                                        "widget": "files",
                                        "string": _("Pictures (EN)"),
                                        "accept": "image/*",
                                        "required": False,
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
                    "name": "destination",
                    "widget": "select",
                    "string": _("Destination"),
                    "required": False,
                    "width": 130,
                },
                {
                    "name": "supplier",
                    "widget": "relation",
                    "displayField": "name",
                    "string": _("Supplier"),
                    "required": False,
                    "width": 140,
                },
                {
                    "name": "activity_type",
                    "widget": "select",
                    "string": _("Act. Type"),
                    "required": False,
                    "width": 110,
                },
                {
                    "name": "duration",
                    "widget": "select",
                    "string": _("Duration"),
                    "required": False,
                    "width": 100,
                },
                {
                    "name": "time",
                    "widget": "select",
                    "string": _("Time"),
                    "required": False,
                    "width": 110,
                },
                {
                    "name": "quality",
                    "widget": "select",
                    "string": _("Quality"),
                    "required": False,
                    "width": 100,
                },
                {
                    "name": "price_range",
                    "widget": "select",
                    "string": _("Price Range"),
                    "required": False,
                    "width": 120,
                },
                {
                    "name": "sell_prc_adult",
                    "widget": "number",
                    "string": _("Sell PRC Ad."),
                    "required": False,
                    "width": 110,
                },
                {
                    "name": "net_prc_adult",
                    "widget": "number",
                    "string": _("Net PRC Ad."),
                    "required": False,
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
                    "name": "smoker_allowed",
                    "string": _("Smoker Allowed"),
                    "filter": {
                        "field": "smoker_friendly",
                        "operator": "eq",
                        "value": "allowed",
                    },
                },
                {
                    "name": "kids_1plus",
                    "string": _("Kids 1+"),
                    "filter": {
                        "field": "children_eligibility",
                        "operator": "eq",
                        "value": "1+",
                    },
                },
                {
                    "name": "kids_3plus",
                    "string": _("Kids 3+"),
                    "filter": {
                        "field": "children_eligibility",
                        "operator": "in",
                        "value": ["1+", "3+"],
                    },
                },
            ],
        },
        {
            "operation": "append",
            "target": "search.group_by",
            "content": [
                {
                    "name": "destination",
                    "string": _("destination"),
                },
                {
                    "name": "supplier",
                    "string": _("Supplier"),
                },
                {
                    "name": "activity_type",
                    "string": _("Act. Type"),
                },
                {
                    "name": "duration",
                    "string": _("Duration"),
                },
                {
                    "name": "quality",
                    "string": _("Quality"),
                },
                {
                    "name": "price_range",
                    "string": _("Price Range"),
                },
                {
                    "name": "time",
                    "string": _("Time"),
                },
            ],
        },
    ],
}
