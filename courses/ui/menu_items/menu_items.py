# -*- coding: utf-8 -*-
# Menu items for courses module

{
    "courses_main_menu": {
        "name": "courses",
        "icon": "BookOpen",
        "module": "courses",
        "sequence": 102,
        'children': {                       #1st gen
            
            "courses_child_menu_courses": {
                "name": "Courses",
                "icon": "Book",
                "module": "courses",
                "sequence": 1,
                "children": {           #2nd gen
                    "courses_gchild_menu_courses": {
                        "name": "Courses",
                        "icon": "Book",
                        "module": "courses",
                        "view_types": "list,form,kanban,graph,search",
                        "model": "courses.courses",
                        "sequence": 1,
                        'actions' : [],
                    },
                    "courses_gchild_menu_level": {
                        "name": "Level",
                        "icon": "TrendingUp",
                        "module": "courses",
                        "view_types": "list,form,kanban,graph,search",
                        "model": "courses.level",
                        "sequence": 2,
                    }
                }
            },

            "courses_child_menu_package": {
                "name": "Package",
                "icon": "Package",
                "module": "courses",
                "model": "courses.package",
                "view_types": "list,form,kanban,graph,search",
                "sequence": 2,
                'actions' : [],
               
            },

            "courses_child_menu_category": {
                "name": "Category",
                "icon": "Layers",
                "module": "courses",
                "model": "courses.category",
                "view_types": "list,form,kanban,graph,search",
                "sequence": 3,
            }
        }
    }
}