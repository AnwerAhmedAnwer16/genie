from django.utils.translation import gettext as _
transport_list_view = {
    "key": "tourism_transport_list_view",
    "menu_item": "tourism_gchild_menu_transport",
    "name": "tourism transport list view",
    "model": "tourism.transport",
    "view_type": "list",
    "priority": 21,
    'module': 'tourism',
    'body': {
        'tree': {
            'fields': [
                {
                    'name': 'tour',
                    'widget': 'relation',
                    'string': _('Tour'),
                },
                {
                    'name': 'type',
                    'widget': 'selection',
                    'string': _('Type'),
                },
                {
                    'name': 'capacity',
                    'widget': 'integer',
                    'string': _('Capacity'),
                }
            ]
        }
    }
}


transport_form_view = {
    "key": "tourism_transport_form_view",
    "name": "Tourism Transport Form",
    "menu_item": "tourism_gchild_menu_transport",
    "model": "tourism.transport",
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
                    {"name": "tour", "widget": "relation"},
                    {"name": "type", "widget": "selection"},
                    {
                        "name": "capacity",
                        "widget": "number",
                        "required": False
                    }
                ]
            },

            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Transport Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "type", "widget": "selection"},
                                {"name": "capacity", "widget": "number"}
                            ]
                        },
                        {
                            "title": "Tour Info",
                            "fullWidth": False,
                            "fields": [
                                {"name": "tour", "widget": "relation"}
                            ]
                        }
                    ]
                }
            ],
            "tabs": [
                {
                    "title": "Details",
                    "sections": [
                        {
                            "title": "Transport Information",
                            "groups": [
                                {
                                    "title": "Additional Info",
                                    "fullWidth": True,
                                    "fields": [
                                        {"name": "type", "widget": "selection"},
                                        {"name": "capacity", "widget": "integer"},
                                        {"name": "tour", "widget": "relation"}
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


transport_kanban_view = {
    "key": "tourism_transport_kanban_view",
    "menu_item": "tourism_gchild_menu_transport",
    "name": "tourism transport kanban view",
    "model": "tourism.transport",
    "view_type": "kanban",
    "priority": 22,
    "module": "tourism",
    "body": {
        "kanban": {
            "id": "tour-transport-kanban",
            "name": "Tour Transport Kanban",
            "description": "Kanban view for tourism transports",
            "group_by": {
                "name": "type",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "type", "tag": "field", "widget": "selection"}
                    },
                    "fields": [
                        {"name": "capacity", "tag": "field", "widget": "integer"},
                        {"name": "tour", "tag": "field", "widget": "relation"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "tour", "tag": "field", "widget": "relation"},
                    ],
                }
            }
        }
    }
}

transport_graph_view = {
    "key": "tourism_transport_graph_view",
    "menu_item": "tourism_gchild_menu_transport",
    "name": "tourism transport graph view",
    "model": "tourism.transport",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'type',
                    'string': _('Transport Type'),
                },
                {
                    'name': 'tour',
                    'string': _('Tour'),
                },
            ],
            'measures': [
                {
                    'name': 'capacity',
                    'string': _('Total Capacity'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'type',
                'measure': 'sum',
            }
        }
    }
}