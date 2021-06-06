from odoo import api, fields, models

# This is a class for the credit limit of the customer calculations


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(string="Credit Limit")
    amount_available = fields.Float(string="Amount Available", compute="_compute_amount_available")
    total_receivable = fields.Float(string="Total Receivable", compute="_compute_total_receivable")
    total_payable = fields.Float(string="Total Payable", compute="_compute_total_payable")
    partner_balance = fields.Float(string="Balance", compute="_compute_partner_balance")

    def _compute_total_payable(self):
        self.total_payable = self.debit

    def _compute_total_receivable(self):
        self.total_receivable = self.credit

    def _compute_partner_balance(self):
        self.partner_balance = self.credit - self.debit

    def _compute_amount_available(self):
        self.amount_available = self.credit_limit - self.partner_balance



