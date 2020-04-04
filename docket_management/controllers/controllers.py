# -*- coding: utf-8 -*-
from odoo import http

# class DocketManagement(http.Controller):
#     @http.route('/docket_management/docket_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/docket_management/docket_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('docket_management.listing', {
#             'root': '/docket_management/docket_management',
#             'objects': http.request.env['docket_management.docket_management'].search([]),
#         })

#     @http.route('/docket_management/docket_management/objects/<model("docket_management.docket_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('docket_management.object', {
#             'object': obj
#         })