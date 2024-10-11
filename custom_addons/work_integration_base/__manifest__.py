{
    "name": "Work Timesheet Management",
    "summary": "Work Timesheet Management",
    "category": "Long Bui",
    "author": "Long Bui",
    "website": "https://www.longbui.net",
    "depends": ["work_timesheet"],
    "license": "LGPL-3",
    "data": [
        # DATA
        # SECURITY
        "security/project_security.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/work_integration.xml",
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
