# -*- coding: utf-8 -*-
{
    'name': "picking_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fahim",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sales_team',
        'account_payment',  # -> account, payment, portal
        'utm',"sale"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "report/ir_action_report.xml",
        "report/ir_actions_report_templates.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
