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

class resource(osv.osv):

    _name = 'resource'
    _description = 'This is a resource, can be a Film or a serie'
 
    _columns = {
            'name':fields.char('Name', size=64, required=True, readonly=False),
            'year':fields.date('Year', required=True),
            'image': fields.binary("Image"),
            'osd':fields.many2one("osd", "OSD", required=True),
            'director': fields.many2one('partaker', 'Director', required=True),
            'scores':fields.one2many("score", "resource_id", "Scores"),
        }
