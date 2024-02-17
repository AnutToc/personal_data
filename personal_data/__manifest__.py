{
    "name": "Personal Data",
    "version": "1.0.0",
    "application": True,
    "depends": ["base", "report_xlsx"],
    "data": [
        "security/ir.model.access.csv",
        "views/personal_data_views.xml",
        "views/personal_data_menus.xml",
        "data/report_paperformat.xml",
        "report/personal_data_templates.xml",
        "report/personal_data_reports.xml",
    ],
    "installable": True,
    'license': 'LGPL-3',
}
