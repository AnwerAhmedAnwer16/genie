# -*- coding: utf-8 -*-
{
    'name': 'courses',
    'summary': 'this is the courses module',
    'description': """
this is the courses module
""",
    'author': "Genie ERP",
    'website': "https://www.aigeniecrm.com",
    'category': 'Courses',
    'version': '0.0.1',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'crm','chatbot'],
    'groups': [
        
        {
            'name': 'Courses  Users',
            'technical_name': 'courses.users',
            'description': 'Access his courses module',
            'category': 'Courses',
        },
        {
            'name': ' Courses Admins',
            'technical_name': 'courses.admins',
            'category': 'Courses',
            'implied_groups': ['courses.users'],
            'description': 'Manage all courses module',
        }
    ]
    
}
