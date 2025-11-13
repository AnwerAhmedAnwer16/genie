from django.utils.translation import gettext as _

review_list_view = {
    "key": "tourism_review_list_view",
    "menu_item": "tourism_gchild_menu_review",
    "name": "tourism review list view",
    "model": "tourism.review",
    "view_type": "list",
    "priority": 21,
    'module': 'tourism',
    'body': {
        'tree': {
            'fields' : [
                {
                    'name' : 'tour',
                    'widget' : 'relation',
                    'string' : _('Tour'),
                },
                {
                    'name' : 'user',
                    'widget' : 'relation',
                    'string' : _('User'),
                },
                {
                    'name' : 'rating',
                    'widget' : 'star',
                    'string' : _('Rating')
                },
                {
                    'name' : 'comment',
                    'widget' : 'text',
                    'string' : _('Comment')
                },
                {
                    'name' : 'created_at',
                    'widget' : 'datetime',
                    'string' : _('Created At')
                }
                ]
                }
                }
                }  



review_form_view = {
    "key": "tourism_review_form_view",
    "name": "Tourism Review Form",
    "model": "tourism.review",
    "view_type": "form",
    "body": {
        "header": {
            "status": {
                "name": "category",
                "widget": "status",
                "string": "Status",
                "help": "Current workflow status"
            },
            
        },

        "sheet": {
            "title": {
                "fields": [
                    {"name": "tour", "widget": "relation"},
                    {"name": "user", "widget": "relation"},
                    {
                        "name": "rating",
                        "widget": "star",
                        "required": False
                    }
                ]
            },

            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Review Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "comment", "widget": "textarea"},
                                {"name": "rating", "widget": "star"}
                            ]
                        },
                        {
                            "title": "Tour Info",
                            "fullWidth": False,
                            "fields": [
                                {"name": "tour", "widget": "relation"},
                                {"name": "user", "widget": "relation"}
                            ]
                        }
                    ]
                }
            ],
            "tabs": [
                {
                    "title": "Comments",
                    "sections": [
                        {
                            "title": "User Feedback",
                            "groups": [
                                {
                                    "title": "Additional Info",
                                    "fullWidth": True,
                                    "fields": [
                                        {"name": "comment", "widget": "textarea"},
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



# review_form_view = {
#     'key': 'tourism_review_form_view',
#     'menu_item': 'tourism_gchild_menu_review',
#     'name': 'tourism review form view',
#     'model': 'tourism.review',
#     'view_type': 'form',
#     'priority': 21,
#     'module': 'tourism',
#     'body': {
#         "header": {
#             "status": {
#                 "name": "category",
#                 "widget": "status",
#                 "string": "Status",
#                 "help": "Current workflow status"
#             },
            
#         },

#         'sheet': {
#             'sections': [
#                 {
#                 "title": "Basic Information",
#                     'groups': [
#                         {
#                             'fields': [
#                                 {
#                                     'name': 'tour',
#                                     'string': 'Tour',
#                                     'widget': 'relation',
#                                     'required': True,
#                                 },
#                                 {
#                                     'name': 'user',
#                                     'string': 'User',
#                                     'widget': 'relation',
#                                     'required': True,
#                                 }
#                             ]
#                         },
#                         {
#                             'fields': [
#                                 {
#                                     'name': 'rating',
#                                     'string': 'Rating',
#                                     'widget': 'star',
#                                     'required': True,
#                                 },
#                                 {
#                                     'name': 'comment',
#                                     'string': 'Comment',
#                                     'widget': 'textarea',
#                                     'required': False,
#                                 },
#                                 {
#                                     'name': 'created_at',
#                                     'string': 'Created At',
#                                     'widget': 'datetime',
#                                     'required': False,
#                                 }
#                             ]
#                         }
#                     ]
#                 }
#             ]
#         }
#     }
# }

review_kanban_view = {
    "key": "tourism_review_kanban_view",
    "menu_item": "tourism_gchild_menu_review",
    "name": "tourism review kanban view",
    "model": "tourism.review",
    "view_type": "kanban",
    "priority": 22,
    "module": "tourism",
    "body": {
        "kanban": {
            "id": "tour-review-kanban",
            "name": "Tour Review Kanban",
            "description": "Kanban view for tourism reviews",
            "group_by": {
                "name": "category",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "user.name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "rating", "tag": "field", "widget": "star"},
                        {"name": "created_at", "tag": "field", "widget": "datetime"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "comment", "tag": "field", "widget": "textarea"},
                        {"name": "tour", "tag": "field", "widget": "relation"},
                    ],
                }
            }
        }
    }
}

review_graph_view = {
    "key": "tourism_review_graph_view",
    "menu_item": "tourism_gchild_menu_review",
    "name": "tourism review graph view",
    "model": "tourism.review",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
        {
            'name': 'tour',
            'string': _('Tour'),
        },
        {
            'name': 'user',
            'string': _('User'),
        },
    ],                  
    'measures': [ 
        {
            'name' : 'rating',
            'string' : _('Rating'),
            'tag': 'field',}      
    ],
    'defaults': {
        'view': 'bar',
        'field': 'tour',
        'measure': 'average',
    }
}
}
}
