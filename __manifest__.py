# -*- coding: utf-8 -*-
{
    'name': "Libreria",
    'summary': 'Gestion de una libreria',
    'description': 'Mi modulo permite gestionar libros, autores, y demas...',
    'author': 'Borja Avalos',
    'website': 'http://www.google.es',
    'category': 'Libros',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_libro.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "application": True
}
