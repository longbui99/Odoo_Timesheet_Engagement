from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Engagement(models.Model):
    _name = "project.engagement"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Engagement"

    def default_manager(self) -> None:
        return self.env.user.employee_id.id

    def default_stage(self) -> None:
        default_stage = self.env.ref("work_timesheet.engagement_open")
        if not default_stage:
            default_stage = self.env["project.engagement.stage"].search(
                [("key", "=", "open")], limit=1
            )
        if not default_stage:
            default_stage = self.env["project.engagement.stage"].search([], limit=1)
        return default_stage.id

    name = fields.Char(
        string="Name",
        required=True, copy=False, readonly=True,
        index='trigram',
        default=lambda self: _('New'))
    partner_id = fields.Many2one("res.partner", string="Client", required=True)
    manager_id = fields.Many2one(
        "hr.employee", string="Manager", default=default_manager
    )
    contract_ids = fields.One2many("project.contract", "engagement_id", string="Contracts")
    project_ids = fields.One2many("project.project", "engagement_id", string="Projects")
    stage_id = fields.Many2one(
        "project.engagement.stage",
        string="Stage",
        default=default_stage,
        required=True,
    )
    company_id = fields.Many2one("res.company", required=True, default=lambda self:self.env.company.id)
    budget = fields.Float(string="Budget", compute="compute_budget")

    def compute_budget(self):
        self.mapped('contract_ids')
        for record in self:
            record.budget = sum(record.mapped('contract_ids.budget'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _("New")) == _("New"):
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'project.engagement') or _("New")
        return super().create(vals_list)


class EngagementStage(models.Model):
    _name = "project.engagement.stage"
    _description = "Project Engagement Stage"
    _order = "id asc"

    name = fields.Char(string="Name", required=True)
    key = fields.Char(string="Key", required=True)
    company_id = fields.Many2one("res.company",
        string="Company", required=True, default=lambda self: self.env.company.id
    )

    @api.constrains('key')
    def check_unique_key(self) -> None:
        for record in self:
            if self.search_count([("key", "=", record.key)]) > 1:
                raise ValidationError(f"Key {record.key} must be unique")
