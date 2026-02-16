# -*- coding: utf-8 -*-
{
    'name': 'awtar',
    'technical_name': 'awtar',
    'type': 'app',
    'summary': 'Awtar - Cost per person for tourism packages',
    'description': """
Awtar module - extends tourism packages with cost per person calculation
based on total purchase orders divided by package seats.
""",
    'author': "Genie ERP",
    'website': "https://www.aigeniecrm.com",
    'category': 'Tourism',
    'version': '0.0.1',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': [
        'tourism',
        'purchase',
    ],
}
