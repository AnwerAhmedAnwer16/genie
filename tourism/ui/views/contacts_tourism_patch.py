
contacts_partner_list_view_patch_v2 = {
    "key": "contacts_partner_list_view_patch_v2",
    "name": "Contacts Partner List View Patch",
    "model": "base.partner",
    "view_type": "list",
    "priority": 22,  
    "inherit_mode": "extension",
    "inherit_id": "contacts_partner_list_view",  
    "module": "contacts",
    "inheritance_operations": [
        {
            "operation": "append",
            "target": "tree.fields",
            "content": [
                {
                    "name": "tours",
                    "string": "tour",
                    "widget": "text",
                    "required": False,
                    "readonly": True,
                },
            ],
        },
    ],
}
