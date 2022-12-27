from odoo import fields, models, api


class SaleEstimateWizard(models.TransientModel):
    _name = 'job.estimation.wizard'
    _description = 'Job estimation wizard'

    customer = fields.Many2one('res.partner', string='Customer', compute='_compute_customer')
    price_list = fields.Many2one('product.pricelist', string='Pricelist')
    related_job_cost_sheet = fields.Many2one('job.cost.sheet',
                                             string='Related job cost sheet')

    @api.depends('related_job_cost_sheet')
    def _compute_customer(self):
        job_cost = self.env['job.cost.sheet'].search([
            ('id', '=', self.related_job_cost_sheet.id)])
        self.customer = job_cost.customer.id

    def create_estimate(self):
        estimation = self.env['estimation.jobs'].create({
            'customer_id': self.customer.id,
            'price_list_id': self.price_list.id,
            'job_cost_sheet': self.related_job_cost_sheet.id
        })

        material_sheet = self.env['page.material'].search([
            ('connection1', '=', self.related_job_cost_sheet.id)])
        for material in material_sheet:
            estimation.write({
                'material_estimation_ids': [(
                    0, 0, {
                        'type': 'Material',
                        'product_id': material.product.id,
                        'quantity': material.planned_qty,
                        'description': material.product.name,
                        'subtotal': material.cost_price_sub_total,
                    }
                )]
            })

        labour_sheet = self.env['page.labour'].search([
            ('connection2', '=', self.related_job_cost_sheet.id)])
        for labour in labour_sheet:
            estimation.write({
                'labour_estimation_ids': [(
                    0, 0, {
                        'type': 'Labour',
                        'product_id': labour.product.id,
                        'quantity': labour.hours,
                        'description': labour.product.name,
                        'subtotal': labour.cost_price_sub_total,
                    }
                )]
            })

        overhead_sheet = self.env['page.overhead'].search([
            ('connection3', '=', self.related_job_cost_sheet.id)])
        for overhead in overhead_sheet:
            estimation.write({
                'overhead_estimation_ids': [(
                    0, 0, {
                        'type': 'Overhead',
                        'product_id': overhead.product.id,
                        'quantity': overhead.planned_qty,
                        'description': overhead.product.name,
                        'subtotal': overhead.cost_price_sub_total,
                    }
                )]
            })
