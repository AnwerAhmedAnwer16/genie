GROUPS = [
    {
        'name' : 'Tourism Useres',
        'technical_name' : 'tourism.users',
        'category' : 'tourism',
        'description' : 'tourism users',
    },




    {
        'name' : 'Tourism Managers',
        'technical_name' : 'tourism.managers',
        'category' : 'tourism',
        'implied_groups' : ['tourism.users'],
        'description' : 'tourism managers', 
    },






    {
        'name' : 'Tourism Admins',
        'technical_name' : 'tourism.admins',
        'category' : 'tourism',
        'implied_groups' : ['tourism.managers'],
        'description' : 'tourism admins',
    }
]