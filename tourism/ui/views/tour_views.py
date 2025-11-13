# -*- coding: utf-8 -*-
# UI Views for tourism module
from django.utils.translation import gettext as _

tour_list_view = {
    "key": "tourism_tour_list_view",
    "menu_item": "tourism_gchild_menu_tour",
    "name": "tourism list view",
    "model": "tourism.tour",
    "view_type": "list",
    "priority": 20,
    'module': 'tourism',
    "body": {
                "tree": {
            "fields": [
                {
                    "name": "id",
                    "widget": "number",
                    "string": _("ID"),
                    "help": True,
                    "formatter": "number"
                },
                {
                    "name": "name", 
                    "widget": "text",
                    "string": _("Name"),
                    "help": "Primary contact name",
                },
                {
                    "name": "description", 
                    "widget": "text",
                    "string": _("description"),
                    "help": "Primary email contact",
                },
                {
                    "name": "price",
                    "widget" : "text",
                    "string": _("price"),
                    "help": "Primary phone contact",
                },
                {
                    "name": "available_seats",
                    "string": _("available_seats"),
                    "help": "Last login date",
                    "widget": "start_date",
                }
            ]
        }
    }
}

tour_form_view = {
    'key' : 'tourism_tour_form_view',
    'menu_item' : 'tourism_gchild_menu_tour',
    'name' : 'tourism form view',
    'model' : 'tourism.tour',
    'view_type' : 'form',
    'priority' : 20,
    'module' : 'tourism',
    "body": {

        "sheet": {
            
            "groups": [
                {
                    # "title": "Customer Information",
                    "groups": [
                        {
                            # "title": "",
                            "fields": [
                                {
                                    "name": "name",
                                    "string": "Name",
                                    "widget": "text",
                                    "required": True,
                                    "readonly": False,
                                    "help": "Tag name",
                                    "placeholder": "Name",
                                    "minLength": None,
                                    "maxLength": None
                                },
                                # {
                                #     "name": "destination",
                                #     "string": "destination",
                                #     "widget": "relation",
                                #     "required": False,
                                #     "readonly": False,
                                #     "help": "destination",
                                # },
                                {
                                    "name": "description",
                                    "string": "Description",
                                    "widget": "textarea",
                                    "required": False,
                                    "readonly": False,
                                    "help": "Color of the tag",
                                    "placeholder": "description",
                                }
                               
                            ]
                        },
                        {
                            # "title": "",
                            "fields": [
                                {
                                    "name": "price",
                                    "string": "price",
                                    "widget": "number",
                                    "required": False,
                                    "readonly": False,
                                    "help": "Description of the tag",
                                    "placeholder": "price",
                                    "onChange": True,
                                },
                                {
                                    "name": "duration_days",
                                    "string": "Duration Days",
                                    "widget": "number",
                                    "required": False,
                                    "readonly": False,
                                    "help": "Sequence of the tag",
                                    "placeholder": "Duration Days",
                                    "min": 0,
                                    "step": 1
                                },
                                {
                                    'name' : 'available_seats',
                                    'widget' : 'number',
                                    "required": False,
                                    "readonly": False,
                                    "help": "Sequence of the tag",
                                    "placeholder": "available seats",
                                    "min": 0,
                                    "step": 1
                                },

                                {
                                    'name' : 'start_date',
                                    'widget' : 'date',
                                    "required": False,
                                    "readonly": False,
                                    "help": "Sequence of the tag",
                                    # "placeholder": "available seats",
                                    "min": 0,
                                    "step": 1
                                }
                            ]
                        }
                    ]
                },
                
            ],
        }
   
    }
}

tour_kanban_view = {
    "key": "tourism_tour_kanban_view",
    "menu_item": "tourism_gchild_menu_tour",
    "name": "tourism kanban view",
    "model": "tourism.tour",
    "view_type": "kanban",
    "priority": 22,
    'module': 'tourism',
    "body": {
        "kanban": {
            'id' : 'tour-kanban',
            'name' : 'Tour Named',
            'description' : 'this is kanban tour',
            # 'group_by': {
            #     'name' : 'name',
            #     'tag' : 'field' 
            # },
            'card' : {
                'header' : {
                    'profile':{
                        'title' : {'name' : 'name' , 'tag': 'field', 'widget' : 'text'}
                        },

                    'fields':[
                        {'name' : 'name' , 'tag': 'field', 'widget' : 'text'},
                        {'name' : 'price' , 'tag': 'field', 'widget' : 'number'},
                        {'name' : 'available_seats' , 'tag': 'field', 'widget' : 'number'},

                    ],
                    "divider": True, 


                },
                'body' :{
                    'fields' : [
                        {'name' : 'name' , 'tag': 'field', 'widget' : 'text'},
                        {'name' : 'price' , 'tag': 'field', 'widget' : 'number'},
                        {'name' : 'available_seats' , 'tag': 'field', 'widget' : 'number'},

                    ],
                }
            }
        }
    }
}


tour_graph_view = {
    "key": "tourism_tour_graph_view",
    "menu_item": "tourism_gchild_menu_tour",
    "name": "tourism graph view",
    "model": "tourism.tour",
    "view_type": "graph",
    "priority": 23,
    'module': 'tourism',
    "body": {
        'graph': {
            'fields': [
        {
            'name': 'name',
            'string': _('Name'),
        },
        {
            'name': 'user',
            'string': _('User'),
        },
        {
            'name' : 'start_date',
            'string' : _('Start Date'),
            'interval' : ['month'],
        }
    ],
    'measures': [
        {
            'name': 'available_seats',
            'string': _('Available Seats'),
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


tour_search_view = {
    "key": "tourism_tour_search_view",
    "menu_item": "tourism_gchild_menu_tour",
    "name": "tourism search view",
    "model": "tourism.tour",
    "view_type": "search",
    "priority": 24,
    'module': 'tourism',
    "body": {
        "search": {
            "search_fields": [
                {
                    "name": ["name"],
                    "widget": "text",
                    "string": _("Name"),
                },
              
                    {
                        'name' : ['price'],
                        'widget' : 'number',
                        'string' : _('Price'),
                    }
            ]
            
        }
    }
}
