GROUPS = [
    {
        'name' : 'courses Useres',
        'technical_name' : 'courses.users',
        'category' : 'courses',
        'description' : 'courses users',
    },




    {
        'name' : 'courses Managers',
        'technical_name' : 'courses.managers',
        'category' : 'courses',
        'implied_groups' : ['courses.users'],
        'description' : 'courses managers', 
    },






    {
        'name' : 'courses Admins',
        'technical_name' : 'courses.admins',
        'category' : 'courses',
        'implied_groups' : ['courses.managers'],
        'description' : 'courses admins',
    }
]