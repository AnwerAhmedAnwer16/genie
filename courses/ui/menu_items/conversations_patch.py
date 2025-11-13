menu_dict = {
    "append_courses_action_omnichannel": {
        "_inherit": "chat_main_menu_omnichannel",
        "inheritance_operations": [
            {
                "operation": "append",
                "target": "actions",
                "content":{
                    "string":"courses",
                    "icon": "book",
                    "name": "get_courses",
                    "type": "server", # server, url, menu
                    'as':'button', # dropdown, button
                    "view_type": ["form"],
                    "confirm_required": False,
                },
            },
        ]
    }
}
