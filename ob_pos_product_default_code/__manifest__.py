# -*- coding: utf-8 -*-

{
    'name': 'PoS Product Internal Reference',
    'author': 'Odoo Bin',
    'company': 'Odoo Bin',
    'maintainer': 'Odoo Bin',
    'description': """ Display product internal reference in point of sale interface | internal reference in pos order line,
    Product reference in receipt pos""",
    'summary': """This module allow you to display product internal reference in point of sale interface and Receipt
""",
    'version': '16.0',
    'license': 'OPL-1',
    'depends': ['point_of_sale'],
    'category': 'Point of Sale',
    'demo': [],
    'assets': {
            'point_of_sale.assets': [
                'ob_pos_product_default_code/static/src/js/models.js',
                'ob_pos_product_default_code/static/src/xml/**/*',
            ],
    },
    'live_test_url': 'https://youtu.be/ygY83w5MQ5o',
    'images': ['static/description/banner.png'],
    "price": 3.49,
    "currency": 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
