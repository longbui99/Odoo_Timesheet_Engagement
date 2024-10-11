from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_employee_cost_id = fields.Many2one(comodel_name='project.employee.cost', string="Project Employee Map")
