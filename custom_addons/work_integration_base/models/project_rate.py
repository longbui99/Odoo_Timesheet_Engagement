from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectRate(models.Model):
    _name = "project.rate"
    _inherit = ['project.rate', 'work.integration.base']
