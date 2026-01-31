# -*- coding: utf-8 -*-
"""
Security groups for yalla_thailand module

This file defines all security groups for the yalla_thailand module.
Groups are synced to the database using the sync_groups management command.
"""

GROUPS = [
    {
        'name': 'Yalla_thailand Users',
        'technical_name': 'yalla_thailand.users',
        'category': 'Yalla_thailand',
        'description': 'Access yalla_thailand module',
    },
    {
        'name': 'Yalla_thailand Admins',
        'technical_name': 'yalla_thailand.admins',
        'category': 'Yalla_thailand',
        'implied_groups': ['yalla_thailand.users'],
        'description': 'Manage all yalla_thailand module',
    }
]
