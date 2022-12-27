{
    'name': "Sale Estimate from Job Cost Sheet",
    'version': '16.0.1.0.0',
    'summary': """Sale Estimate from Job Cost Sheet""",
    'description': 'Sale Estimate from Job Cost Sheet',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'project_job_costing', 'estimation_for_jobs'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_estimate_wizard_view.xml',
        'views/job_cost_sheet_inherit_view.xml',
    ],
    # 'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
