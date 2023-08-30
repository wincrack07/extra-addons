odoo.define('pos_salesperson.models', function(require){
    'use strict';
    var { Orderline } = require('point_of_sale.models');
	var core = require('web.core');
    const Registries = require('point_of_sale.Registries');
	var _t = core._t;
    //
    const PosSaleOrderline = (Orderline) => class PosSaleOrderline extends Orderline {
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            if (json.user_id) {
                var user = this.get_user_by_id(json.user_id);
                if (user) {
                    this.set_line_user(user);
                }
            }
        }
        set_line_user (user) {
            this.user_id = user;
        }
        get_line_user () {
            if (this.user_id && this.user_id.id !== undefined) {
                return this.user_id;
            }
            return null;
        }
        get_user_image_url () {
            if (this.user_id && this.user_id.id !== undefined) {
                return window.location.origin + '/web/image?model=res.users&field=image_128&id=' + this.user_id.id;
            }
            return null;
        }
        remove_sale_person () {
            this.user_id = null;
        }
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            if (this.user_id) {
                json.user_id = this.user_id.id;
            }
            return json;
        }
        get_user_by_id (user_id) {
            var self = this;
            var user = null;
            for (var i = 0; i < self.pos.user.length; i++) {
                if (self.pos.user[i].id == user_id) {
                    user = self.pos.user[i];
                }
            }
            return user;
        }
    }
    Registries.Model.extend(Orderline, PosSaleOrderline);

});
