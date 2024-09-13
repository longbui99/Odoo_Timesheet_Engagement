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
