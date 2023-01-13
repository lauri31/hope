# SDG
from datetime import datetime
from odoo import api, fields, models, _, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string='Fax')





