from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    test = fields.Char("Test")
