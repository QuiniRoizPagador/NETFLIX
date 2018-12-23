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

class partaker(osv.osv):

    _name = 'partaker'
    _description = 'this is a partaker from a resource.'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'country':fields.many2one("res.country", "Country", required=True),
            'birth':fields.date('Birth'),
            'image': fields.binary("Image"),
            'series_actor':fields.many2many('serie','serie_partaker_rel','partaker_id','serie_id','Series'),
            'films_actor':fields.many2many('film','film_partaker_rel','partaker_id','film_id','Films'),
            'series_director':fields.one2many("serie", "director", "Series Director"),
            'films_director':fields.one2many("film", "director", "Films Director"),
        }
    _sql_constraints = [     ('name_uniq', 'unique (name)', 'The Name of the Partaker must be unique !'),      ]