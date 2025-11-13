from django.utils.translation import gettext as _

guide_list_view = {
    "key": "tourism_guide_list_view",
    "menu_item": "tourism_child_menu_guide",
    "name": "tourism guide list view",
    "model": "tourism.guide",
    "view_type": "list",
    "priority": 21,
    'module': 'tourism',
    'body': {
        'tree': {
            'fields': [
                {
                    'name': 'name',
                    'widget': 'text',
                    'string': _('Name'),
                },
                {
                    'name': 'phone',
                    'widget': 'text',
                    'string': _('Phone'),
                },
                {
                    'name': 'email',
                    'widget': 'text',
                    'string': _('Email'),
                },
                {
                    'name': 'tours',
                    'widget': 'relation',
                    'string': _('Tours')
                }
            ]
        }
    }
}


guide_form_view = {
    "key": "tourism_guide_form_view",
    "menu_item": "tourism_child_menu_guide",
    "name": "Tourism Guide Form",
    "model": "tourism.guide",
    "view_type": "form",
    "body": {
        # "header": {
        #     "status": {
        #         "name": "tours",
        #         "widget": "status",
        #         "string": "Status",
        #         "help": "Current workflow status"
        #     },
        # },

        "sheet": {
            "title": {
                "fields": [
                    {"name": "name", "widget": "text"},
                    {"name": "phone", "widget": "text"},
                    {
                        "name": "email",
                        "widget": "text",
                        "required": False
                    }
                ]
            },

            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Contact Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "phone", "widget": "text"},
                                {"name": "email", "widget": "text"}
                            ]
                        },
                        {
                            "title": "Biography",
                            "fullWidth": False,
                            "fields": [
                                {"name": "bio", "widget": "textarea"}
                            ]
                        }
                    ]
                }
            ],
            "tabs": [
                {
                    "title": "Tours",
                    "sections": [
                        {
                            "title": "Assigned Tours",
                            "groups": [
                                {
                                    "title": "Tour List",
                                    "fullWidth": True,
                                    "fields": [
                                        {"name": "tours", "widget": "relation"},
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Additional Info",
                    "sections": [
                        {
                            "title": "Biography",
                            "groups": [
                                {
                                    "title": "About",
                                    "fullWidth": True,
                                    "fields": [
                                        {"name": "bio", "widget": "textarea"},
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}


guide_kanban_view = {
    "key": "tourism_guide_kanban_view",
    "menu_item": "tourism_child_menu_guide",
    "name": "tourism guide kanban view",
    "model": "tourism.guide",
    "view_type": "kanban",
    "priority": 22,
    "module": "tourism",
    "body": {
        "kanban": {
            "id": "tour-guide-kanban",
            "name": "Tour Guide Kanban",
            "description": "Kanban view for tourism guides",
            "group_by": {
                "name": "name",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "phone", "tag": "field", "widget": "text"},
                        {"name": "email", "tag": "field", "widget": "text"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "bio", "tag": "field", "widget": "textarea"},
                    ],
                }
            }
        }
    }
}

guide_graph_view = {
    "key": "tourism_guide_graph_view",
    "menu_item": "tourism_child_menu_guide",
    "name": "tourism guide graph view",
    "model": "tourism.guide",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('Guide'),
                },
                {
                    'name': 'tours',
                    'string': _('Tours'),
                },
            ],
            'measures': [
                {
                    'name': 'tours',
                    'string': _('Number of Tours'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'name',
                'measure': 'count',
            }
        }
    }
}
################################# end of guide views #####################
