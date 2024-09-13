from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectContract(models.Model):
    _name = "project.contract"
    _inherit = ['project.contract', 'work.integration.base']
