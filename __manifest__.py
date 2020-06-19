# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sample Project',
    'version': '1.0',
    'category': 'ISGM',
    'sequence': 75,
    'summary': 'Sample Project',
    'description': """

You can manage:
---------------
    """,
    'website': '',
    'images': [
      
    ],
    'depends': [
        'base_setup', 'web' , 'base', 'mail'

    ],
    'data': [
        
        'security/sample_project_security.xml',
        'security/ir.model.access.csv',
        'views/test1.xml',
        
        'report/report_paperformat.xml',
        'report/report_test.xml',
        'report/test_report.xml',
        
        'wizard/test_wizard_view.xml',
        
        'views/test_scheduler.xml',
    ],
    'demo': [],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
