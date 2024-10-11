from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = ['project.project', 'work.integration.base']