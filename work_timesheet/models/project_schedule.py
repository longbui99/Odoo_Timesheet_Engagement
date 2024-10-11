from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Schedule(models.Model):
    _name = "project.schedule"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Schedule"

    role_id = fields.Many2one("project.role", string="Role", required=True)
    employee_id = fields.Many2one("hr.employee", related="role_id.employee_id", string="Employee", required=True)
    project_id = fields.Many2one("project.project", string="Project", required=True)
    date = fields.Date(string="Scheduled Date")
    schedule_hour = fields.Float(string="Schedule Hour")
