from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PropjectTask(models.Model):
    _inherit = "project.task"

    is_required_description = fields.Boolean(string="Is Required Description?", default=True)
    rate_id = fields.Many2one("project.rate", string="Rate")
