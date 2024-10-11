from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectEngagement(models.Model):
    _name = "project.engagement"
    _inherit = ['project.engagement', 'work.integration.base']
