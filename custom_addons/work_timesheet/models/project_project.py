from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Propject(models.Model):
    _inherit = "project.project"

    engagement_id = fields.Many2one("project.engagement", string="Engagement")
    contract_id = fields.Many2one("project.contract", string="Contract")
    rate_ids = fields.One2many("project.rate", "project_id", string="Rates")
    rate_count = fields.Integer(string="Rate Count", compute="compute_rate_count")

    role_ids = fields.One2many("project.role", "project_id", string="Roles")
    role_count = fields.Integer(string="Role Count", compute="compute_role_count")

    schedule_ids = fields.One2many("project.schedule", "project_id", string="Schedule")
    schedule_count = fields.Integer(string="Schedule Count", compute="compute_schedule_count")
    sequence_id = fields.Many2one(
        'ir.sequence', 'Reference Sequence',
        check_company=True, copy=False)
    sequence_code = fields.Char('Sequence Prefix', required=True, copy=False)
    cost_employee_ids = fields.One2many("project.employee.cost", "project_id", string="Employee Cost")
    is_required_description = fields.Boolean(string="Is Required Description?", default=True)

    def compute_rate_count(self):
        self.mapped("rate_ids")
        for record in self:
            record.rate_count = len(record.rate_ids)

    def compute_role_count(self):
        self.mapped("role_ids")
        for record in self:
            record.role_count = len(record.role_ids)

    def compute_schedule_count(self):
        self.mapped("schedule_ids")
        for record in self:
            record.schedule_count = len(record.schedule_ids)
    
    @api.depends('sequence_code', 'name')
    def _compute_display_name(self):
        for project in self:
            project.display_name = f'[{project.sequence_code}] {project.name}'

    # ================================================= PREPARE VALUES ===============================
    
    def prepare_sale_order_line_values(self, data_map):
        return {
            'name': data_map.product_id.name,
            'product_uom_qty': quantity,
            'product_id': data_map.product_id and line.product_id.id or False,
            'product_uom': data_map.product_id and line.product_id.uom_id.id or line.product_uom.id,
            'price_unit': price,
            'company_id': self.company_id.id,
        }

    def prepare_sale_order_values(self):
        so_metadata = {
            'partner_id': self.partner_id,
        }
        line_datas = []
        for sale_map in self.cost_employee_ids:
            pass

        

    # ================================================= ACTION =======================================

    def action_view_rates(self):
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "work_timesheet.action_project_rate"
        )
        action["domain"] = [("project_id", "in", self.ids)]
        action["context"] = {"default_project_id": self.id}
        return action

    def action_view_roles(self):
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "work_timesheet.action_project_role"
        )
        action["domain"] = [("project_id", "in", self.ids)]
        action["context"] = {"default_project_id": self.id}
        return action

    def action_view_schedules(self):
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "work_timesheet.action_project_schedule"
        )
        action["domain"] = [("project_id", "in", self.ids)]
        action["context"] = {"default_project_id": self.id}
        return action

    def action_create_sale_order(self):
        self.ensure_one()
        values = self.prepare_sale_order_values()
        self.env['sale.order'].create(values)

    # ======================== CURD ============================
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('sequence_id') and vals.get('sequence_code'):
                vals['sequence_id'] = self.env['ir.sequence'].sudo().create({
                    'name': _('Sequence') + ' ' + vals['sequence_code'],
                    'prefix': vals['sequence_code'] + "-", 
                    'padding': 3,
                    'company_id': vals.get('company_id') or self.env.company.id,
                }).id
        return super().create(vals_list)
    
    def write(self, vals):
        if 'sequence_code' in vals:
            for project in self:
                project.sequence_id.sudo().write({
                    'name': _('Sequence') + ' ' + vals['sequence_code'],
                    'prefix': vals['sequence_code'] + "-", 'padding': 3,
                    'company_id': project.env.company.id,
                })
        return super().write(vals)