# -*- coding: utf-8 -*-
{
    'name': 'yalla_thailand',
    'technical_name': 'yalla_thailand',
    'type': 'app',
    'summary': 'Yalla Thailand customizations for Tourism ERP',
    'description': """
Yalla Thailand module - extends tourism, account, sales, and purchase modules
with package type fields and localized attachment fields.
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
        'account',
        'sales',
        'purchase',
    ],
}
