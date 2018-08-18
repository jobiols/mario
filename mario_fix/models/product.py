# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def action_open_quants(self):
        return
