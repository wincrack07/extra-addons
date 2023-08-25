# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_show_customer_details = fields.Boolean(string='Show Customer Details On POS Receipt')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_show_customer_details = fields.Boolean(related='pos_config_id.pos_show_customer_details',readonly=False)
