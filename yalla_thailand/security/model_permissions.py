# -*- coding: utf-8 -*-
"""
Access rights for yalla_thailand module.
Format: [view, add, change, delete] as [0/1, 0/1, 0/1, 0/1]
"""

MODEL_PERMISSIONS = [
    # Example: Model1
    # {
    #     'model': 'yalla_thailand.modelname',
    #     'group': 'yalla_thailand.users',
    #     'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    # },
    # {
    #     'model': 'yalla_thailand.modelname',
    #     'group': 'yalla_thailand.admins',
    #     'permissions': [1, 1, 1, 1],  # full access
    # },
]

# Permission patterns for convenience
PERMISSION_PATTERNS = {
    'NONE': [0, 0, 0, 0],           # No access
    'VIEW_ONLY': [1, 0, 0, 0],      # View only
    'MANAGE': [1, 1, 1, 0],         # Manage but no delete
    'FULL': [1, 1, 1, 1],           # Full access
}

# Example using patterns:
# {
#     'model': 'yalla_thailand.modelname',
#     'group': 'yalla_thailand.users',
#     'permissions': PERMISSION_PATTERNS['MANAGE'],
# }
