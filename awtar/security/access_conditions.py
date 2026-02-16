# -*- coding: utf-8 -*-
"""
Access conditions for awtar module.

Format for each condition:
{
    "name": "Human readable name",
    "model": "app.model",  # Model this condition applies to
    "condition": {         # Filter condition in ERPFilterRequest format
        "operator": "and",
        "filters": [
            {"field": "field_name", "operator": "eq", "value": "value"},
            # ... more filters
        ]
    },
    "groups": ["group.technical.name"],  # Optional: groups this applies to (empty = global)
    "permissions": [1, 1, 1, 0],  # [view, add, change, delete] as [0/1, 0/1, 0/1, 0/1]
}
"""

from modules.base.utils.filter_schema import create_own_records_condition, create_true_field_condition

ACCESS_CONDITIONS = [
    # Example: Users can only view/edit their own records
    # {
    #     "name": "my records only",
    #     "model": "awtar.modelname",
    #     "condition": create_own_records_condition('assigned_to'),
    #     "permissions": [1, 1, 1, 0],  # View, Add, Change, No Delete
    #     "groups": ["awtar.users"],
    # },
]
