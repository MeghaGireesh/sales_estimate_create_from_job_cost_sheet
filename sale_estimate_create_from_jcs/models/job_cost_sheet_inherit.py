from odoo import models, fields


class JobCostSheetInherit(models.Model):
    _inherit = 'job.cost.sheet'

    def view_sale_estimates(self):
        return {
            'name': 'Sale Estimate',
            'view_mode': 'tree,form',
            'res_model': 'estimation.jobs',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('job_cost_sheet', '=', self.id)],
        }


class EstimateINherit(models.Model):
    _inherit = 'estimation.jobs'

    job_cost_sheet = fields.Many2one('job.cost.sheet',
                                     string='Related Job cost sheet')

    def smart_job_cost_sheet(self):
        print('aaaaaaaa')
        return {
            'name': 'Job Cost Sheets',
            'view_mode': 'tree,form',
            'res_model': 'job.cost.sheet',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('id', '=', self.job_cost_sheet.id)],
        }


