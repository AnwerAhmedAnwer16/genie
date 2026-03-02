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
        # 1. Trip Info fields (left group) - Destination, categories, timing
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
                },
                {
                    "name": "destination",
                    "widget": "select",
                    "string": _("Destination"),
                },
                {
                    "name": "act_type",
                    "widget": "select",
                    "string": _("Act. Type"),
                },
                {
                    "name": "duration",
                    "widget": "select",
                    "string": _("Duration"),
                },
                {
                    "name": "time",
                    "widget": "select",
                    "string": _("Time"),
                },
                {
                    "name": "stop_act",
                    "widget": "select",
                    "string": _("Stop/Act."),
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
                },
                {
                    "name": "price_range",
                    "widget": "select",
                    "string": _("Price Range"),
                },
                {
                    "name": "lunch",
                    "widget": "select",
                    "string": _("Lunch"),
                },
                {
                    "name": "longtail_boat",
                    "widget": "select",
                    "string": _("Longtail Boat"),
                },
                {
                    "name": "national_park",
                    "widget": "select",
                    "string": _("National Park"),
                },
                {
                    "name": "no_of_pax",
                    "widget": "select",
                    "string": _("No. of PAX"),
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
                                    },
                                    {
                                        "name": "weather_sensitivity",
                                        "widget": "select",
                                        "string": _("Weather Sensitivity"),
                                    },
                                    {
                                        "name": "children_eligibility",
                                        "widget": "select",
                                        "string": _("Children Eligibility"),
                                    },
                                    {
                                        "name": "stability",
                                        "widget": "select",
                                        "string": _("Stability"),
                                    },
                                ],
                            },
                            {
                                "fields": [
                                    {
                                        "name": "action_adrenaline",
                                        "widget": "select",
                                        "string": _("Action Adrenaline"),
                                    },
                                    {
                                        "name": "romantic_honeymoon",
                                        "widget": "select",
                                        "string": _("Romantic / Honeymoon"),
                                    },
                                    {
                                        "name": "smoker_friendly",
                                        "widget": "select",
                                        "string": _("Smoker Friendly"),
                                    },
                                    {
                                        "name": "mobility",
                                        "widget": "select",
                                        "string": _("Mobility"),
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
                                    },
                                    {
                                        "name": "boat_view",
                                        "widget": "select",
                                        "string": _("Boat View"),
                                    },
                                    {
                                        "name": "water_act",
                                        "widget": "select",
                                        "string": _("Water Act."),
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
                                    },
                                    {
                                        "name": "net_prc_adult",
                                        "widget": "number",
                                        "string": _("Net PRC Ad."),
                                    },
                                    {
                                        "name": "min_markup",
                                        "widget": "number",
                                        "string": _("Min. Markup"),
                                    },
                                ],
                            },
                            {
                                "fields": [
                                    {
                                        "name": "sell_prc_child",
                                        "widget": "number",
                                        "string": _("Sell PRC Ch."),
                                    },
                                    {
                                        "name": "net_prc_child",
                                        "widget": "number",
                                        "string": _("Net PRC Ch."),
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
                                    {
                                        "name": "note",
                                        "widget": "text",
                                        "string": _("Note"),
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
                    "name": "destination",
                    "widget": "select",
                    "string": _("Destination"),
                    "width": 130,
                },
                {
                    "name": "supplier",
                    "widget": "relation",
                    "displayField": "name",
                    "string": _("Supplier"),
                    "width": 140,
                },
                {
                    "name": "act_type",
                    "widget": "select",
                    "string": _("Act. Type"),
                    "width": 110,
                },
                {
                    "name": "duration",
                    "widget": "select",
                    "string": _("Duration"),
                    "width": 100,
                },
                {
                    "name": "time",
                    "widget": "select",
                    "string": _("Time"),
                    "width": 110,
                },
                {
                    "name": "quality",
                    "widget": "select",
                    "string": _("Quality"),
                    "width": 100,
                },
                {
                    "name": "price_range",
                    "widget": "select",
                    "string": _("Price Range"),
                    "width": 120,
                },
                {
                    "name": "sell_prc_adult",
                    "widget": "number",
                    "string": _("Sell PRC Ad."),
                    "width": 110,
                },
                {
                    "name": "net_prc_adult",
                    "widget": "number",
                    "string": _("Net PRC Ad."),
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
                    "string": _("Destination"),
                },
                {
                    "name": "supplier",
                    "string": _("Supplier"),
                },
                {
                    "name": "act_type",
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
