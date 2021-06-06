from odoo import models, fields, api, _


class SalesCreditCheck(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    total_receivable = fields.Float(related="partner_id.total_receivable", string="Total Receivable")
    total_payable = fields.Float(related="partner_id.total_payable", string="Total Payable")
