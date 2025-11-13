from django.utils.translation import gettext as _

tour_booking_list_view = {
    "key": "tourism_booking_list_view",
    "menu_item": "tourism_gchild_menu_tour_booking",
    "name": "tourism booking list view",
    "model": "tourism.tourbooking",
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
                    'name' : 'seats_booked',
                    'widget' : 'number',
                    'string' : _('Seats')
                },
                {
                    'name' : 'booking_date',
                    'widget' : 'datetime',
                    'string' : _('Booking Date')
                },
                {
                    'name' : 'paid',
                    'widget' : 'boolean',
                    'string' : _('Paid')
                }
            ]
        }
    }
}

tour_booking_form_view = {
    'key' : 'tourism_booking_form_view',
    'menu_item' : 'tourism_gchild_menu_tour_booking',
    'name' : 'tourism booking form view',
    'model' : 'tourism.tourbooking',
    'view_type' : 'form',
    'priority' : 21,
    'module' : 'tourism',
    'body' : {
        'sheet' : {
            'groups' : [
                {
                    'groups' : [
                        {
                            'fields' : [
                                {
                                    'name' : 'tour',
                                    'string' : 'Tour',
                                    'widget' : 'relation',
                                    'required' : True,
                                },
                                {
                                    'name' : 'user',
                                    'string' : 'User',
                                    'widget' : 'relation',
                                    'required' : True,
                                }
                            ]
                        },
                        {
                            'fields' : [
                                {
                                    'name' : 'seats_booked',
                                    'string' : 'Seats Booked',
                                    'widget' : 'number',
                                    'required' : True,
                                },
                                {
                                    'name' : 'booking_date',
                                    'string' : 'Booking Date',
                                    'widget' : 'datetime',
                                    'required' : True,
                                },
                                {
                                    'name' : 'paid',
                                    'string' : 'Paid',
                                    'widget' : 'switch',
                                    'required' : False,
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
tour_booking_kanban_view = {
    "key": "tourism_booking_kanban_view",
    "menu_item": "tourism_gchild_menu_tour_booking",
    "name": "tourism booking kanban view",
    "model": "tourism.tourbooking",
    "view_type": "kanban",
    "priority": 22,
    'module': 'tourism',
    "body": {
        "kanban": {
            'id' : 'tour-booking-kanban',
            'name' : 'Tour Booking Named',
            'description' : 'this is kanban tour booking',
            'group_by': {
                'name' : 'tour',
                'tag' : 'field' 
            },
            'card' : {
                'header' : {
                    'profile':{
                        'title' : {'name' : 'tour.name' , 'tag' : 'field', 'widget' : 'text'}
                        },

                    'fields':[
                        {'name' : 'seats_booked' , 'tag': 'field', 'widget' : 'number'},
                        {'name' : 'booking_date' , 'tag': 'field', 'widget' : 'date'},
                        {'name' : 'paid' , 'tag': 'field', 'widget' : 'boolean'},

                    ],
                    "divider": True, 


                },
                'body' :{
                    'fields' : [
                        {'name' : 'seats_booked' , 'tag': 'field', 'widget' : 'number'},
                        {'name' : 'booking_date' , 'tag': 'field', 'widget' : 'date'},
                        {'name' : 'paid' , 'tag': 'field', 'widget' : 'boolean'},

                    ],
                }
            }
        }
    }
}   


tour_booking_graph_view = {
    "key": "tourism_booking_graph_view",
    "menu_item": "tourism_gchild_menu_tour_booking",
    "name": "tourism booking graph view",
    "model": "tourism.tourbooking",
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
            'name' : 'seats_booked',
            'string' : _('Seats Booked'),
            'tag': 'field',}      
    ],
    'defaults': {
        'view': 'bar',
        'field': 'tour',
        'measure': 'count',
    }
}
}
}
tour_booking_search_view = {
    "key": "tourism_booking_search_view",
    "menu_item": "tourism_gchild_menu_tour_booking",
    "name": "tourism booking search view",
    "model": "tourism.tourbooking",
    "view_type": "search",
    "priority": 24,
    'module': 'tourism',
    "body": {
        "search": {
            "search_fields": [
                {
                    "name": ["tour__name"],
                    "widget": "text",
                    "string": _("Tour"),
                },
                {
                    'name' : ['user__username'],
                    'widget' : 'text',
                    'string' : _('User'),
                },
                {
                    'name' : ['seats_booked'],
                    'widget' : 'number',
                    'string' : _('Seats Booked'),
                }
            ]
            
        }
    }
}
########################### end of tour booking views ##########################    
