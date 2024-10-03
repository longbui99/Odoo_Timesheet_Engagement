from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.constrains('description')
    def check_missing_description(self) -> None:
        error_lines = self.filtered(lambda line: line.task_id.is_required_description and not line.description)
        if error_lines:
            raise ValidationError("Missing Description")