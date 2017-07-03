# -*- coding: utf-8 -*-
from odoo import http

# class Role(http.Controller):
#     @http.route('/role/role/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/role/role/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('role.listing', {
#             'root': '/role/role',
#             'objects': http.request.env['role.role'].search([]),
#         })

#     @http.route('/role/role/objects/<model("role.role"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('role.object', {
#             'object': obj
#         })