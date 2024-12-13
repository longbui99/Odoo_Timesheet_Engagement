from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    estimated_amount = fields.Monetary(string="Delivered Amount", compute="_compute_estimated_amount")

    def _compute_estimated_amount(self):
        for order in self:
            order.estimated_amount = sum([line.qty_delivered*line.price_unit for line in self.order_line])

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _timesheet_create_task_prepare_values(self, project):
        vals = super()._timesheet_create_task_prepare_values(project)
        names = self.name.split("\n")
        if len(names) > 1:
            vals['name'] = '%s - %s' % (self.order_id.name or '', names[1])
        return vals