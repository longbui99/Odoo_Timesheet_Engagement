from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class WorkIntegrationBase(models.Model):
    _name = "work.integration"
    _description = "Work Integration Base"

    name = fields.Char(string="Name", required=True)
    key = fields.Char(string="Key", required=True)

    @api.constrains('key')
    def check_unique_key(self) -> None:
        for record in self:
            if self.search_count([("key", "=", record.key)]) > 1:
                raise ValidationError(f"Key {record.key} must be unique")

    # def update_selection_values(self):
    #     field = self.env.ref('work_integration_base.field_project_engagement__integration_source')
    #     if field:
    #         integrations = self.search([])
    #         res = [fields.Command.create({
    #             'value': integration.key,
    #             'name': integration.name
    #         }) for integration in integrations]
    #         res.append({'value': '', 'name': ''})
    #         field.selection_ids = [fields.Command.set([])] + res

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super().create(vals)
    #     res.update_selection_values()
    #     return res

    # def write(self, vals):
    #     res = super().write(vals)
    #     self.update_selection_values()
    #     return res
    
    # def unlink(self):
    #     res = super().unlink()
    #     self.update_selection_values()
    #     return res