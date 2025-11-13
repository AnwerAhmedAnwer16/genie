from django.utils.translation import gettext as _
category_list_view = {
    "key": "tourism_category_list_view",
    "menu_item": "tourism_gchild_menu_category",
    "name": "tourism category list view",
    "model": "tourism.category",
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
                    'name': 'description',
                    'widget': 'text',
                    'string': _('Description'),
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


category_form_view = {
    "key": "tourism_category_form_view",
    "menu_item": "tourism_gchild_menu_category",
    "name": "Tourism Category Form",
    "model": "tourism.category",
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
                    {
                        "name": "description",
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
                            "title": "Category Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                            ]
                        },
                        {
                            "title": "Description",
                            "fullWidth": False,
                            "fields": [
                                {"name": "description", "widget": "textarea"}
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
                            "title": "Associated Tours",
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
                            "title": "Details",
                            "groups": [
                                {
                                    "title": "About Category",
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


category_kanban_view = {
    "key": "tourism_category_kanban_view",
    "menu_item": "tourism_gchild_menu_category",
    "name": "tourism category kanban view",
    "model": "tourism.category",
    "view_type": "kanban",
    "priority": 22,
    "module": "tourism",
    "body": {
        "kanban": {
            "id": "tour-category-kanban",
            "name": "Tour Category Kanban",
            "description": "Kanban view for tourism categories",
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
                        {"name": "name", "tag": "field", "widget": "text"},
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

category_graph_view = {
    "key": "tourism_category_graph_view",
    "menu_item": "tourism_gchild_menu_category",
    "name": "tourism category graph view",
    "model": "tourism.category",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('Category'),
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
