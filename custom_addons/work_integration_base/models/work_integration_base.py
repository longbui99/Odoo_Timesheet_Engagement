
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class WorkIntegrationBase(models.AbstractModel):
    _name = "work.integration.base"
    _description = "Work Integration Base"

    integration_source = fields.Char(string="Source", inverse="_set_integration")
    integration_id = fields.Many2one("work.integration", string="Integration")

    def _set_integration(self):
        keys = self.mapped('integration_source')
        integrations = self.env['work.integration'].search([('key', 'in', keys)])
        integration_by_key = dict()
        for integration in integrations:
            integration_by_key[integration.key] = integration

        for record in self:
            if record.integration_source in integration_by_key:
                record.integration_id = integration_by_key[record.integration_source]
