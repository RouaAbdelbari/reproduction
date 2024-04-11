# -*- coding: utf-8 -*-
{
    'name': "reproduction",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','board','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/vache.xml',
        'views/tech.xml',
        'views/listetech.xml',
        'views/ferme.xml',
        'views/ecurie.xml',
        'views/formulaireecurie.xml',
        'views/insiform.xml',
        'views/insimu.xml',
        'views/chaleur.xml',
        'data/data.xml',
        'views/dashboard.xml',
        'report/rapport.xml',
        'report/vachedeta.xml',
        'report/rapporttech.xml',
        'report/insirapport.xml'
    ],
  
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

