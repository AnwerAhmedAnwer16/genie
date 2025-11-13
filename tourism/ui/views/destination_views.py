from django.utils.translation import gettext as _
destination_list_view = {
    "key": "tourism_destination_list_view",
    "menu_item": "tourism_gchild_menu_destination",
    "name": "tourism destination list view",
    "model": "tourism.destination",
    "view_type": "list",
    "priority": 21,
    'module': 'tourism',
    'body': {
        'tree': {
            'fields': [
                {
                    'name': 'image',
                    'widget': 'image',
                    'string': _('Image'),
                },
                {
                    'name': 'name',
                    'widget': 'text',
                    'string': _('Name'),
                },
                {
                    'name': 'city',
                    'widget': 'text',
                    'string': _('City'),
                },
                {
                    'name': 'country',
                    'widget': 'text',
                    'string': _('Country'),
                },
                {
                    'name': 'created_at',
                    'widget': 'datetime',
                    'string': _('Created At')
                }
            ]
        }
    }
}


destination_form_view = {
    "key": "tourism_destination_form_view",
    "name": "Tourism Destination Form",
    "menu_item": "tourism_gchild_menu_destination",
    "model": "tourism.destination",
    "view_type": "form",
    "body": {
        # "header": {
        #     "status": {
        #         "name": "category",
        #         "widget": "status",
        #         "string": "Status",
        #         "help": "Current workflow status"
        #     },
        # },

        "sheet": {
            "title": {
                "fields": [
                    {"name": "name", "widget": "text"},
                    {"name": "city", "widget": "text"},
                    {
                        "name": "country",
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
                            "title": "Location Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "city", "widget": "text"},
                                {"name": "country", "widget": "text"}
                            ]
                        },
                        {
                            "title": "Media",
                            "fullWidth": False,
                            "fields": [
                                {"name": "image", "widget": "image"},
                                {"name": "created_at", "widget": "datetime"}
                            ]
                        }
                    ]
                }
            ],
            "tabs": [
                {
                    "title": "Description",
                    "sections": [
                        {
                            "title": "Destination Details",
                            "groups": [
                                {
                                    "title": "About",
                                    "fullWidth": True,
                                    "fields": [
                                        {"name": "description", "widget": "textarea"},
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


destination_kanban_view = {
    "key": "tourism_destination_kanban_view",
    "menu_item": "tourism_gchild_menu_destination",
    "name": "tourism destination kanban view",
    "model": "tourism.destination",
    "view_type": "kanban",
    "priority": 22,
    "module": "tourism",
    "body": {
        "kanban": {
            "id": "tour-destination-kanban",
            "name": "Tour Destination Kanban",
            "description": "Kanban view for tourism destinations",
            "group_by": {
                "name": "name",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"},
                        "image": {"name": "image", "tag": "field", "widget": "image"}
                    },
                    "fields": [
                        {"name": "city", "tag": "field", "widget": "text"},
                        {"name": "country", "tag": "field", "widget": "text"},
                        {"name": "created_at", "tag": "field", "widget": "datetime"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "description", "tag": "field", "widget": "textarea"},
                    ],
                }
            }
        }
    }
}

destination_graph_view = {
    "key": "tourism_destination_graph_view",
    "menu_item": "tourism_gchild_menu_destination",
    "name": "tourism destination graph view",
    "model": "tourism.destination",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'country',
                    'string': _('Country'),
                },
                {
                    'name': 'city',
                    'string': _('City'),
                },
                {
                    'name': 'name',
                    'string': _('Destination'),
                },
            ],
            'measures': [
                {
                    'name': 'name',
                    'string': _('Number of Destinations'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'country',
                'measure': 'count',
            }
        }
    }
}
