# -*- coding: utf-8 -*-
##############################################################################
#
# This module is developed by Deddy Setiawan
# Copyright (C) 2017 Deddy Setiawan (<http://dedset.xyz>).
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Invoice In words',
    'version' : '1.0.0.0.1',
    'summary': 'Adds in words on invoice total',
    'author' : 'Deddy Setiawan',
    'category': 'Sale',
    'description': """
    - Adds in words on invoice total
    """,
    'license':'LGPL-3',
    'depends' : ['base', 'sale',],
    'data': [
        'views/account_invoice_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
