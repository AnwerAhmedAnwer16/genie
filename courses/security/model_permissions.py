# courses/security/model_permissions.py
"""
Access rights for courses module.
Format: [view, add, change, delete] as [0/1, 0/1, 0/1, 0/1]
"""

MODEL_PERMISSIONS = [
    # Category
    {
        'model': 'courses.category',
        'group': 'courses.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'courses.category',
        'group': 'courses.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Level
    {
        'model': 'courses.level',
        'group': 'courses.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'courses.level',
        'group': 'courses.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Package
    {
        'model': 'courses.package',
        'group': 'courses.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'courses.package',
        'group': 'courses.admins',
        'permissions': [1, 1, 1, 1],  # full access
    },
    
    # Courses
    {
        'model': 'courses.courses',
        'group': 'courses.users',
        'permissions': [1, 1, 1, 0],  # view, add, change, no delete
    },
    {
        'model': 'courses.courses',
        'group': 'courses.admins',
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
