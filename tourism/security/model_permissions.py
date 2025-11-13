# tourism/security/model_permissions.py
"""
Access rights for tourism module.
Format: [view, add, change, delete] as [0/1, 0/1, 0/1, 0/1]
"""

MODEL_PERMISSIONS = [
    # Destination
    {
        'model': 'tourism.destination',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.destination',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Tour
    {
        'model': 'tourism.tour',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.tour',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Category
    {
        'model': 'tourism.category',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.category',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Guide
    {
        'model': 'tourism.guide',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.guide',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Review
    {
        'model': 'tourism.review',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.review',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Tourbooking
    {
        'model': 'tourism.tourbooking',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.tourbooking',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Transport
    {
        'model': 'tourism.transport',
        'group': 'tourism.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'tourism.transport',
        'group': 'tourism.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
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
#     'model': 'app.model',
#     'group': 'app.users',
#     'permissions': PERMISSION_PATTERNS['MANAGE'],
# }
