from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectEmployeeCost(models.Model):
    _name = "project.employee.cost"
    _inherit = 'project.sale.line.employee.map'


    def product_domain(self):
        return [
            ('type', '=', 'service'),
        ]

    cost_from = fields.Float("Cost From")
    employee_id = fields.Many2one(required=False, domain="[('id', 'in', existing_employee_ids)]")
    sale_line_id = fields.Many2one(required=False)
    product_id = fields.Many2one("product.product", string="Service", domain=product_domain)

    def _compute_existing_employee_ids(self):
        project = self.project_id
        if len(project) == 1:
            self.existing_employee_ids = project.sale_line_employee_ids.employee_id
            return
        for map_entry in self:
            map_entry.existing_employee_ids = map_entry.project_id.role_ids.employee_id