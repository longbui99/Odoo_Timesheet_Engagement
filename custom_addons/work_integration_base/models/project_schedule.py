from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectSchedule(models.Model):
    _name = "project.schedule"
    _inherit = ['project.schedule', 'work.integration.base']
