# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = 'pos.config'

    allow_salesperson = fields.Boolean('Allow Salesperson')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_salesperson = fields.Boolean(related='pos_config_id.allow_salesperson',readonly=False)

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_users(self):
        return {
            'search_params': {
                # 'domain': [('id', '=', self.env.user.id)],
                'domain': [('share', '=', False)],
                'fields': ['name', 'groups_id'],
            },
        }

    def _get_pos_ui_res_users(self, params):
        user = self.env['res.users'].search_read(**params['search_params'])[0]
        user['role'] = 'manager' if any(id == self.config_id.group_pos_manager_id.id for id in user['groups_id']) else 'cashier'
        del user['groups_id']
        # return user
        return self.env['res.users'].search_read(**params['search_params'])

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def _order_fields(self, ui_order):
        session = self.env['pos.session'].browse(ui_order.get('pos_session_id'))
        user_id = False
        if session and session.user_id:
            user_id = session.user_id.id
        ui_order['user_id'] = user_id
        return super(PosOrder, self)._order_fields(ui_order)
