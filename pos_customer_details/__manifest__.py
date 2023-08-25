# -*- coding: utf-8 -*-
{
    'name': "POS Customer Details On Receipt",
    'summary': """POS Customer Details, POS Client Details, POS Receipt, POS Receipt Client Details,
     POS Receipt Customer Details, POS Ticket Details, POS Customer Info, POS Customer Info on Receipt,
     POS Client Info on Receipt, Print Customer Info On POS Receipt""",
    'description': """this is retail feature for any kind of retail businesses""",
    'author': "Khaled Hassan",
    'website': "https://apps.odoo.com/apps/modules/browse?search=Khaled+hassan",
    'currency': 'EUR',
    'price': 7,
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'data': ['views/pos_config_view.xml',],
    'images': ['static/description/main_screenshot.png'],
    'assets': {
        'point_of_sale.assets': [
            'pos_customer_details/static/src/xml/**/*',
        ],
    },
    'installable': True,
    'aplication' : False,
    'license': "OPL-1",
}
