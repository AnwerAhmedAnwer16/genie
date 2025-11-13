from django.utils.translation import gettext as _
level_list_view = {
    "key": "courses_level_list_view",
    "menu_item": "courses_gchild_menu_level",
    "name": "courses level list view",
    "model": "courses.level",
    "view_type": "list",
    "priority": 21,
    'module': 'courses',
    'body': {
        'tree': {
            'fields': [
                {
                    'name': 'name',
                    'widget': 'text',
                    'string': _('Name'),
                },
                {
                    'name': 'order',
                    'widget': 'integer',
                    'string': _('Order'),
                },
                {
                    'name': 'description',
                    'widget': 'text',
                    'string': _('Description'),
                }
            ]
        }
    }
}


level_form_view = {
    "key": "courses_level_form_view",
    "menu_item": "courses_gchild_menu_level",
    "name": "Courses Level Form",
    "model": "courses.level",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "Level Information",
                    "groups": [
                        {
                            "title": "Level Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "order", "widget": "number"},
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
            ]
        }
    }
}
level_kanban_view = {
    "key": "courses_level_kanban_view",
    "menu_item": "courses_gchild_menu_level",
    "name": "courses level kanban view",
    "model": "courses.level",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-level-kanban",
            "name": "Courses Level Kanban",
            "description": "Kanban view for courses levels",
            # "group_by": {
            #     "name": "category",
            #     "tag": "field"
            # },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "order", "tag": "field", "widget": "number"},
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

level_graph_view = {
    "key": "courses_level_graph_view",
    "menu_item": "courses_gchild_menu_level",
    "name": "courses level graph view",
    "model": "courses.level",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('Level'),
                },
                {
                    'name': 'order',
                    'string': _('Order'),
                }
            ],
            'measures': [
                {
                    'name': 'order',
                    'string': _('Level Order'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'name',
                'measure': 'average',
            }
        }
    }
}

level_search_view = {
    "key": "courses_level_search_view",
    "menu_item": "courses_gchild_menu_level",
    "name": "courses level search view",
    "model": "courses.level",
    "view_type": "search",
    "priority": 24,
    'module': 'courses',
    "body": {
        "search": {
            "search_fields": [
                {
                    "name": ["name"],
                    "widget": "text",
                    "string": _("Name"),
                },
                {
                    "name": ["order"],
                    "widget": "number",
                    "string": _("Order"),
                },
                {
                    "name": ["description"],
                    "widget": "text",
                    "string": _("Description"),
                }
            ]
        }
    }
}

