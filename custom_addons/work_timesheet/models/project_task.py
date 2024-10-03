from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PropjectTask(models.Model):
    _inherit = "project.task"

    is_required_description = fields.Boolean(string="Is Required Description?", default=True)
    rate_id = fields.Many2one("project.rate", string="Rate")
    key = fields.Char(string="Key", copy=False)
    project_id = fields.Many2one(required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            defaults = self.default_get(['project_id'])
            project = self.env['project.project'].browse(vals.get('project_id', defaults.get('project_id')))
            if vals.get('key', '/') == '/' and defaults.get('key', '/') == '/' and vals.get('project_id', defaults.get('project_id')):
                if project.sequence_id:
                    vals['key'] = project.sequence_id.next_by_id()
        res = super().create(vals_list)
        res.filtered(lambda task: not task.is_required_description and task.project_id.is_required_description).update({'is_required_description': True})
        return res
    
    @api.depends('key', 'name')
    def _compute_display_name(self):
        for task in self:
            task.display_name = f'[{task.key}] {task.name}'