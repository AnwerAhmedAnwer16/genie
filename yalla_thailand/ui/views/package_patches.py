# -*- coding: utf-8 -*-
"""
Yalla Thailand - Tour Package Form View Patches
Replaces the Attachments tab with 6 separate attachment fields (AR/EN).
"""
from django.utils.translation import gettext as _


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
        {
            "operation": "replace",
            "target": "sheet.tabs.4",
            "content": {
                "title": _("Attachments"),
                "sections": [
                    {
                        "groups": [
                            {
                                "fullWidth": True,
                                "fields": [
                                    {
                                        "name": "audio_ar",
                                        "widget": "files",
                                        "string": _("Audio (AR)"),
                                        "accept": "audio/*"
                                    },
                                    {
                                        "name": "audio_en",
                                        "widget": "files",
                                        "string": _("Audio (EN)"),
                                        "accept": "audio/*"
                                    },
                                    {
                                        "name": "video_ar",
                                        "widget": "files",
                                        "string": _("Video (AR)"),
                                        "accept": "video/*"
                                    },
                                    {
                                        "name": "video_en",
                                        "widget": "files",
                                        "string": _("Video (EN)"),
                                        "accept": "video/*"
                                    },
                                    {
                                        "name": "pics_ar",
                                        "widget": "files",
                                        "string": _("Pictures (AR)"),
                                        "accept": "image/*"
                                    },
                                    {
                                        "name": "pics_en",
                                        "widget": "files",
                                        "string": _("Pictures (EN)"),
                                        "accept": "image/*"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
