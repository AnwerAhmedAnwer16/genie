from django.utils.translation import gettext as _

category_list_view = {
    "key": "courses_category_list_view",
    "menu_item": "courses_child_menu_category",
    "name": "courses category list view",
    "model": "courses.category",
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
                    'name': 'description',
                    'widget': 'text',
                    'string': _('Description'),
                }
            ]
        }
    }
}

category_form_view = {
    "key": "courses_category_form_view",
    "name": "Courses Category Form",
    "menu_item": "courses_child_menu_category",
    "model": "courses.category",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": " Category Information",
                    "groups": [
                        {
                            "title": "Category Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"}
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

category_kanban_view = {
    "key": "courses_category_kanban_view",
    "menu_item": "courses_child_menu_category",
    "name": "courses category kanban view",
    "model": "courses.category",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-category-kanban",
            "name": "Courses Category Kanban",
            "description": "Kanban view for courses categories",
            # "group_by": {
            #     "name": "category",
            #     "tag": "field"
            # },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [],
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
    "key": "courses_category_graph_view",
    "menu_item": "courses_child_menu_category",
    "name": "courses category graph view",
    "model": "courses.category",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('Category'),
                }
            ],
            'measures': [
                {
                    'name': 'name',
                    'string': _('Number of Categories'),
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

category_search_view = {
    "key": "courses_category_search_view",
    "menu_item": "courses_child_menu_category",
    "name": "courses category search view",
    "model": "courses.category",
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
                    "name": ["description"],
                    "widget": "text",
                    "string": _("Description"),
                }
            ]
        }
    }
}



