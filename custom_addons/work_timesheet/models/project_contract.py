from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Contract(models.Model):
    _name = "project.contract"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Contract"

    def default_manager(self) -> None:
        return self.env.user.employee_id.id

    def default_stage(self) -> None:
        default_stage = self.env.ref("work_timesheet.contract_open")
        if not default_stage:
            default_stage = self.env["project.contract.stage"].search(
                [("key", "=", "open")], limit=1
            )
        if not default_stage:
            default_stage = self.env["project.contract.stage"].search([], limit=1)
        return default_stage.id

    name = fields.Char(
        string="Name",
        required=True, copy=False, readonly=False,
        index='trigram',
        default=lambda self: _('New'))
    partner_id = fields.Many2one("res.partner", string="Client", required=True)
    manager_id = fields.Many2one(
        "hr.employee", string="Manager", default=default_manager
    )
    engagement_id = fields.Many2one("project.engagement", string="Engagement")
    project_ids = fields.One2many("project.project", "contract_id", string="Projects")
    stage_id = fields.Many2one(
        "project.contract.stage",
        string="Stage",
        default=default_stage,
        required=True,
    )
    company_id = fields.Many2one("res.company", required=True, default=lambda self:self.env.company.id)
    budget = fields.Float(string="Budget")

    sign_template_ids = fields.Many2many(string="Contract(s)", comodel_name="sign.template", relation="sign_template_contract",
        column1='sign_template_id',
        column2='contract_id',
        )
    signed_document_ids = fields.Many2many(string="Signed Document(s)", comodel_name="sign.request", relation="sign_request_contract",
        column1='sign_template_id',
        column2='contract_id',)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _("New")) == _("New"):
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'project.contract') or _("New")
        return super().create(vals_list)


class ContractStage(models.Model):
    _name = "project.contract.stage"
    _description = "Project Contract Stage"
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
