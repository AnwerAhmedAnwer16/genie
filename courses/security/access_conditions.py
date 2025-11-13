from modules.base.utils.filter_schema import *

ACCESS_CONDITIONS = [
    {
        'name' : 'creator only',
        'model' : 'courses.category',
        'condition' : {
        'filters': {
            "operator": "and",
            "filters": [
                {"field": 'active', "operator": "eq", "value": True}
            ]
        }
    },
        'permissions' : [1, 1, 1, 1],
        'groups' : ['courses.users'],
    },
]