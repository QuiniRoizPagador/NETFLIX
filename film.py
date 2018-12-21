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

class film(osv.Model):
    _name = 'film'
    _description = 'This is a film'
    _inherit = 'resource'
 
    _columns = {
            'premiere_date': fields.date("Premiere Date", required=True, autodate=True),
            'source': fields.char("Source", required=False),
            'film_fav': fields.many2many('upoflix.user', 'user_film_fav', 'film_id','user_id', 'Users Favorites'),
            'actors': fields.many2many('partaker', 'film_partaker_rel', 'film_id', 'partaker_id', 'Actors'),
            'genders': fields.many2many('gender', 'film_gender_rel', 'film_id', 'gender_id', 'Genders', required=True),
            'scores':fields.one2many("score", "film_id", "Scores"),
        }