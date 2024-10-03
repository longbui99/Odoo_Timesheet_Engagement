from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectRole(models.Model):
    _name = "project.role"
    _description = "Project Role"

    name = fields.Char(string="Name", required=True)
    project_id = fields.Many2one("project.project", string="Project", required=True)
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
