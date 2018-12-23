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

class serie(osv.osv):
    _name = 'serie'
    _inherit = 'resource'
    _columns = {
                'finalization_date':fields.date('Finalization Date'),
                'seasons': fields.one2many('season', 'serie_id', 'Seasons'),
                'serie_fav': fields.many2many('upoflix.user', 'user_serie_fav', 'serie_id', 'user_id', 'Users Favorites'),
                'genders': fields.many2many('gender', 'serie_gender_rel', 'serie_id', 'gender_id', 'Genders', required=True),
                'actors': fields.many2many('partaker', 'serie_partaker_rel', 'serie_id', 'partaker_id', 'Actors'),
                'scores':fields.one2many("score", "serie_id", "Scores"),
                 'state':fields.selection([
                                           ("new", "New"),
                                           ("released", "Released"),
                                           ("cancelled", "Cancelled"),
                                           ("finalized", "Finalized"),
                                           ("delayed", "Delayed"),
                                           ], "Status"),
    }
    _defaults = {  
        'state': "new",
        }
