from odoo import api, fields, models

# This is a class for the credit limit of the customer calculations


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(string="Credit Limit")
    amount_available = fields.Float(string="Amount Available")
    total_receivable = fields.Float(string="Total Receivable", stored="False", compute="_compute_try_to_upgrade")

    total_payable = fields.Float(string="Total Payable")
    balance = fields.Float(string="Balance")

    @api.depends("balance", "name")
    def _compute_try_to_upgrade(self):
        self.total_receivable = self.balance
        print(self.balance)
        print("name --------->", self.name)

