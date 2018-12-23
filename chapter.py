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

class chapter(osv.Model):

    _name = 'chapter'
    _description = 'This is a chapter form a season in a serie'
 
    _columns = {
            'name':fields.char('Title', size=64, required=True),
            'description': fields.text('Description'),
            'emission_date': fields.date("Emision Date", required=True, autodate=True),
            'image': fields.binary("Image"),
            'source': fields.char("Source", required=False),
            'season_id':fields.many2one('season', 'Season', ondelete="cascade")
        }
    _sql_constraints = [     ('name_uniq', 'unique (name)', 'The Name of the Chapter must be unique !'), ]
