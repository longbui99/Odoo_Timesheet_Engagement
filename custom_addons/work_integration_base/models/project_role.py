from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectRole(models.Model):
    _name = "project.role"
    _inherit = ['project.role', 'work.integration.base']
