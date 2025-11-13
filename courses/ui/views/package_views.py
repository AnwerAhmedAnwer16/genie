from django.utils.translation import gettext as _

package_list_view = {
    "key": "courses_package_list_view",
    "menu_item": "courses_child_menu_package",
    "name": "courses package list view",
    "model": "courses.package",
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
                    'name': 'price',
                    'widget': 'monetary',
                    'string': _('Price'),
                },
                {
                    'name': 'duration',
                    'widget': 'text',
                    'string': _('Duration'),
                },
                {
                    'name': 'is_active',
                    'widget': 'boolean',
                    'string': _('Active')
                }
            ]
        }
    }
}

package_form_view = {
    "key": "courses_package_form_view",
    "name": "Courses Package Form",
    "menu_item": "courses_child_menu_package",
    "model": "courses.package",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Package Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "price", "widget": "number"},
                                # {"name": "duration", "widget": "text"},
                                {"name": "is_active", "widget": "switch"}
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

package_kanban_view = {
    "key": "courses_package_kanban_view",
    "menu_item": "courses_child_menu_package",
    "name": "courses package kanban view",
    "model": "courses.package",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-package-kanban",
            "name": "Courses Package Kanban",
            "description": "Kanban view for courses packages",
            "group_by": {
                "name": "is_active",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "price", "tag": "field", "widget": "number"},
                        {"name": "duration", "tag": "field", "widget": "text"},
                        {"name": "is_active", "tag": "field", "widget": "switch"},
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

package_graph_view = {
    "key": "courses_package_graph_view",
    "menu_item": "courses_child_menu_package",
    "name": "courses package graph view",
    "model": "courses.package",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('Package'),
                },
                {
                    'name': 'is_active',
                    'string': _('Active Status'),
                }
            ],
            'measures': [
                {
                    'name': 'price',
                    'string': _('Total Price'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'name',
                'measure': 'sum',
            }
        }
    }
}

package_search_view = {
    "key": "courses_package_search_view",
    "menu_item": "courses_child_menu_package",
    "name": "courses package search view",
    "model": "courses.package",
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
                    "name": ["is_active"],
                    "widget": "boolean",
                    "string": _("Active"),
                }
            ]
        }
    }
}


