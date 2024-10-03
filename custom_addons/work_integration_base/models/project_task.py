from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ['project.task', 'work.integration.base']
