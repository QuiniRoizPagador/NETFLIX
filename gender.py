# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class gender(osv.osv):
    _name = 'gender'
    _columns = {
           'name': fields.char("Gender", size=64, required=True),
           'description': fields.text('Description', required=True),
           'films':fields.many2many('film', 'film_gender_rel', 'gender_id', 'film_id', 'Films'),
           'series':fields.many2many('serie', 'serie_gender_rel', 'gender_id', 'serie_id', 'Series'),
    }
    _sql_constraints = [     ('name_uniq', 'unique (name)', 'The Name of the Gender must be unique !'),      ]