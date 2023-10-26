/** @odoo-module **/
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { registry } from "@web/core/registry";

export const SpiffyIconListView = {
   ...listView,
   buttonTemplate: "show_icon_pack",
};

registry.category("views").add("button_in_tree", SpiffyIconListView);