# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'my document manager',
    'summary': 'Aplicación para la gestión de documentos, carpetas y revisiones.',
    'author': 'Sergio Martinez Meneses',
    'company': 'Quetzalcode',
    'maintainer': 'Sergio Martinez Meneses',
    'website': 'https://sergiommq.github.io/portafolio/',
    'category': 'Productividad',
    'version': '1.0.3',
    'description': """
        La aplicación Documentos facilita la gestión eficiente de archivos y documentos, 
        permitiendo organizar y controlar el acceso mediante carpetas y revisiones. 
        Ideal para empresas que requieren un control detallado de documentos internos.
    """,
    'depends': ['base', 'base_setup', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_folder.xml',
        'views/document_search.xml',
        'views/revisiones_documentos.xml',
        'views/document_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'price': 90,
    'currency': 'USD',
    'support': 'quetzal.mq97@gmail.com',
}
