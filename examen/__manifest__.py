# -*- coding: utf-8 -*-
{
    'name': "examen Desiteg",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Jose Nicolielly",
    'website': "http://desiteg.com/portal/",

    'category': 'Examen',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/examen_desiteg_security.xml',
        'views/desiteg_views.xml',
        'data/ir_sequence_data.xml',
        'data/examen_data.xml',
        'report/device_template.xml',
        'report/report_equipos.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
