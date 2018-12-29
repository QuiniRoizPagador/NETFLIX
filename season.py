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

class season(osv.osv):
    
    def removeChapters(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'chapters':[(5,)]}, context=None)

    _name = 'season'
    _description = 'this is a season from a serie.'
 
    _columns = {
            'name':fields.integer("Season", required=True),
            'start_date':fields.date('Start Date'),
            'end_date':fields.date('End Date'),
            'serie_id':fields.many2one('serie', 'Serie', required=True, ondelete="cascade"),
            'chapters':fields.one2many('chapter', 'season_id', 'Chapters'),
        }
    def _check_name(self, cr, uid, ids): 
        return self.browse(cr, uid, ids)[0].name > 0
    
    _constraints = [(_check_name, 'Error: Invalid Season Number', ['name']), ] 
    _sql_constraints = [ ('chapters_uniques', 'unique(name, chapters)', 'The chapter reference must be unique!'),
                         ]
