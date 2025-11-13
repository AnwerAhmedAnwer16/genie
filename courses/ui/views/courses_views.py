from django.utils.translation import gettext as _

courses_list_view = {
    "key": "courses_courses_list_view",
    "menu_item": "courses_gchild_menu_courses",
    "name": "courses courses list view",
    "model": "courses.courses",
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
                    'name': 'level',
                    'widget': 'relation',
                    'string': _('Level'),
                },
                {
                    'name': 'package',
                    'widget': 'relation',
                    'string': _('Package'),
                },
                {
                    'name': 'price',
                    'widget': 'monetary',
                    'string': _('Price')
                },
                {
                    'name': 'duration_hours',
                    'widget': 'float',
                    'string': _('Duration (Hours)')
                },
                {
                    'name': 'is_published',
                    'widget': 'boolean',
                    'string': _('Published')
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


courses_form_view = {
    "key": "courses_courses_form_view",
    "menu_item": "courses_gchild_menu_courses",
    "name": "Courses Form",
    "model": "courses.courses",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Course Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "level", "widget": "relation"},
                                {"name": "package", "widget": "relation"},
                                {"name": "is_published", "widget": "switch"},
                               {"name": "description", "widget": "textarea"}

                            ]
                        },
                        {
                            "title": "Pricing & Duration",
                            "fullWidth": False,
                            "fields": [
                                {"name": "price", "widget": "number"},
                                {"name": "duration_hours", "widget": "number"},
                                {"name": "created_at", "widget": "datetime"}
                            ]
                        }
                    ]
                },
                # {
                #     "title": "Description",
                #     "groups": [
                #         {
                #             "title": "About Course",
                #             "fullWidth": True,
                #             "fields": [
                #                 {"name": "description", "widget": "textarea"}
                #             ]
                #         }
                #     ]
                # }
            ]
        }
    }
}

courses_kanban_view = {
    "key": "courses_courses_kanban_view",
    "menu_item": "courses_gchild_menu_courses",
    "name": "courses courses kanban view",
    "model": "courses.courses",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-courses-kanban",
            "name": "Courses Kanban",
            "description": "Kanban view for courses",
            "group_by": {
                "name": "level",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "price", "tag": "field", "widget": "number"},
                        {"name": "duration_hours", "tag": "field", "widget": "number"},
                        {"name": "is_published", "tag": "field", "widget": "switch"},
                        {"name": "created_at", "tag": "field", "widget": "datetime"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "description", "tag": "field", "widget": "textarea"},
                        {"name": "package", "tag": "field", "widget": "relation"},
                    ],
                }
            }
        }
    }
}

courses_graph_view = {
    "key": "courses_courses_graph_view",
    "menu_item": "courses_gchild_menu_courses",
    "name": "courses courses graph view",
    "model": "courses.courses",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'level',
                    'string': _('Level'),
                },
                {
                    'name': 'package',
                    'string': _('Package'),
                },
                {
                    'name': 'is_published',
                    'string': _('Published Status'),
                }
            ],
            'measures': [
                {
                    'name': 'price',
                    'string': _('Total Price'),
                    'tag': 'field',
                },
                {
                    'name': 'duration_hours',
                    'string': _('Total Duration'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'level',
                'measure': 'sum',
            }
        }
    }
}

courses_search_view = {
    "key": "courses_courses_search_view",
    "menu_item": "courses_gchild_menu_courses",
    "name": "courses courses search view",
    "model": "courses.courses",
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
                    "name": ["price"],
                    "widget": "number",
                    "string": _("Price"),
                },
                {
                    "name": ["duration_hours"],
                    "widget": "number",
                    "string": _("Duration Hours"),
                },
                {
                    "name": ["is_published"],
                    "widget": "boolean",
                    "string": _("Published"),
                }
            ]
        }
    }
}