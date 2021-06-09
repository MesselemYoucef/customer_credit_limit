from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SalesCreditCheck(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    credit_limit = fields.Float(related="partner_id.credit_limit", string="Credit Limit")
    amount_available = fields.Float(related="partner_id.amount_available", string="Amount Available")
    total_receivable = fields.Float(related="partner_id.total_receivable", string="Total Receivable")
    total_payable = fields.Float(related="partner_id.total_payable", string="Total Payable")
    partner_balance = fields.Float(related="partner_id.partner_balance", string="Balance")
    allow_over_credit = fields.Boolean(related="partner_id.allow_over_credit", string="Allow Over Credit")

    @api.constrains('amount_total', 'amount_available', 'allow_over_credit')
    def check_sale_order_illigibility(self):
        for record in self:
            if record.amount_total > record.amount_available and not record.allow_over_credit:
                raise UserError("The sale order total is more than amount available, please check with the finance team")
