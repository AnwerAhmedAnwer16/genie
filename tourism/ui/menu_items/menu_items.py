# -*- coding: utf-8 -*-
# Menu items for tourism module


{
    "tourism_main_menu": {
        "name": "tourism",
        "icon": "MapPin",
        "module": "tourism",
        "sequence": 101,
        # "model" : "tourism.tour",
        # "view_type" : "list",               #should be added 
        'children': {                       #1st gen
            
            "tourism_child_menu_tour": {
                "name": "Tour",
                "icon": "Airplay",
                "module": "tourism",
                # "model": "tourism.tour",
                "sequence": 1,
                "children": {           #2nd gen
                    "tourism_gchild_menu_tour": {
                        "name": "Tour",
                        "icon": "Airplay",
                        "module": "tourism",
                        "view_types" : "list,form,kanban,graph,search",
                        "model": "tourism.tour",
                        "sequence": 1,
                        'actions': [
                            {
                                "name": "discount_by100",
                                "string": "Discount",
                                "icon": "FileText",
                                "type": "server",
                                "view_type" : ["list","kanban"],
                                "confirm_required": True,
                                "as": "dropdown"
                            }
                        ],
                    },
                    "tourism_gchild_menu_tour_booking":
                    {
                        "name": "Tour Booking",
                        "icon": "Book",
                        "module": "tourism",
                        "view_types" : "list,form,kanban,graph,search",
                        "model": "tourism.tourbooking",
                        "sequence": 2,
                    },
                    "tourism_gchild_menu_review":{
                        "name": "Review",
                        "icon": "Star",
                        "module": "tourism",
                        "view_types" : "list,form,kanban,graph,search",
                        "model": "tourism.review",
                        "sequence": 3,   
                    }
                    
                }
            },

            "tourism_child_menu_guide": {
                "name": "guide",
                "icon": "MessageCircle",
                "module": "tourism",
                "model": "tourism.guide",
                "view_types" : "list,form,kanban,graph,search",

                "sequence": 2,
            },
            "tourism_child_menu_destination": {
                "name": "destination",
                "icon": "Compass",
                "module": "tourism",
                # "model": "tourism.destination",
                'allowed_groups': ['tourism.managers'],
                "sequence": 3,
                "children": {       #2nd gen
                    
                    "tourism_gchild_menu_destination": {
                        "name": "Destination",
                        "icon": "Compass",
                        "module": "tourism",
                        "view_types": "list,form,kanban,graph,search",
                        "model": "tourism.destination",
                        "sequence": 1,
                    },
                    
                    "tourism_gchild_menu_category": {
                        "name": "Category",
                        "icon": "Tag",
                        "module": "tourism",
                        "view_types": "list,form,kanban,graph,search",
                        "model": "tourism.category",
                        "sequence": 2,
                    }
                }
            },
            "tourism_gchild_menu_transport": {
                "name": "transport",
                "icon": "Flag",
                "module": "tourism",
                "model": "tourism.transport",
                "view_types" : "list,form,kanban,graph,search",
                "sequence": 4,
            }
        }
    }
}
