# -*- coding: utf-8 -*-
{
    'name': "Smart Binary Solutions",

    'summary': """
        Módulo de Recepción de Productos""",

    'description': """
        Módulo de Recepción de Productos con entrada y salida.
    """,

    'author': "DevFullScoopers",
    'website': "http://www.devfullscoopers.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/res_group.xml',
        'security/ir_rule.xml',
        'security/ir_model_access.xml',
        'report/templates.xml',
        'report/report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
