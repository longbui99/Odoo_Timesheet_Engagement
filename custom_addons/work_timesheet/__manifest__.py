{
    "name": "Work Timesheet Management",
    "summary": "Work Timesheet Management",
    "category": "Long Bui",
    "author": "Long Bui",
    "website": "https://www.longbui.net",
    "depends": ["timesheet_grid", "hr", "project", "sale_timesheet", "sign"],
    "license": "LGPL-3",
    "data": [
        # DATA
        "data/ir_sequence_data.xml",
        "data/contract_data.xml",
        "data/engagement_data.xml",
        # SECURITY
        "security/setup.xml",
        "security/project_security.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/project_engagement_views.xml",
        "views/project_contract_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/project_rate_views.xml",
        "views/project_role_views.xml",
        "views/project_schedule_views.xml",
        # WIZARDS
    ],
    "application": True,
    "assets": {
        "web.assets_backend": [
        ],
    },
}
