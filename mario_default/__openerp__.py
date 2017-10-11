# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'mario',
    'version': '9.0.1.1',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Mario',
    'description': """


Customización Mario
===================
""",
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_afipws_fe',        # Factura Electrónica Argentina
        'l10n_ar_aeroo_einvoice',   # impresion de factura electronica aeroo
        'server_mode',              # habilitar uso de parametro server_mode = "some value" en config.

        'sale',
        'account_accountant',
        'crm'
    ],

    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
