odoo.define('ml_pos_product_arabic.default_code', function (require) {
    "use strict";
    var { Order, Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const DefaultCodePosSaleOrderline = (Orderline) => class DefaultCodePosSaleOrderline extends Orderline {
      constructor(obj, options) {
          super(...arguments);
      }
  export_for_printing() {
    var json = super.export_for_printing(...arguments);
    if (this.get_product().default_code) {
        json.default_code = this.get_product().default_code;
    }
    return json;
  }
  
}
Registries.Model.extend(Orderline, DefaultCodePosSaleOrderline);
});
