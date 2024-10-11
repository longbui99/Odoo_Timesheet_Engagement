from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectRate(models.Model):
    _name = "project.rate"
    _description = "Project Rate"

    name = fields.Char(string="Name", required=True)
    project_id = fields.Many2one("project.project", string="Project", required=True)
    fixed_rate = fields.Float(string="Fixed Rate")
    discount = fields.Float(string="Discount")
