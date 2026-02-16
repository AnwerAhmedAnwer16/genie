# -*- coding: utf-8 -*-
"""
Security groups for awtar module

This file defines all security groups for the awtar module.
Groups are synced to the database using the sync_groups management command.
"""

GROUPS = [
    {
        'name': 'Awtar Users',
        'technical_name': 'awtar.users',
        'category': 'Awtar',
        'description': 'Access awtar module',
    },
    {
        'name': 'Awtar Admins',
        'technical_name': 'awtar.admins',
        'category': 'Awtar',
        'implied_groups': ['awtar.users'],
        'description': 'Manage all awtar module',
    }
]
