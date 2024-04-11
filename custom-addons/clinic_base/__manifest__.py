# -*- coding: utf-8 -*-
{
    'name': "Clinic Management System",
    'summary': "Clinic Management System for managing Hospital and medical facilities flows.",
    'description': """
                A clinic management software or practice management software provides a suite of 
                functionalities that makes it easy to manage a clinic. A medical practice management 
                system is used to manage the patients, the appointments, the doctors' schedules, 
                prescriptions, manage inventory, etc.
    """,
    'author': "Bassam Mannaa",
    'website': "https://odoo-professional.com",
    'support': "b_mannaa@hotmail.com",
    'category': 'Medical',
    'license': 'OPL-1',
    'version': '0.1',
    'depends': ['base','mail'],
    'data': [
        # Security
        'security/clinic_security.xml',
        'security/ir.model.access.csv',

        # data
        'data/physician_degree_data.xml',
        'data/physician_specialty_data.xml',


        # Views
        'views/physician_degree.xml',
        'views/physician_speciality.xml',
        'views/physician.xml',

        # Menu
        'views/menu.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
    'sequence': 1,
    'price': 36,
    'currency': 'USD',
}
