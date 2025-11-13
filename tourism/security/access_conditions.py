from modules.base.utils.filter_schema import *

ACCESS_CONDITIONS = [
    {
        'name' : 'creator tours only',
        'model' : 'tourism.tour',
        'condition' : {
        'filters': {
            "operator": "and",
            "filters": [
                {"field": 'active', "operator": "eq", "value": True}
            ]
        }
    },
        'permissions' : [1, 1, 1, 1],
        'groups' : ['tourism.users'],
    },
]