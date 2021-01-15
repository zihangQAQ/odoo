# -*- coding: utf-8 -*-
# from odoo import http


# class mcrm(http.Controller):
#     @http.route('/mcrm/mcrm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mcrm/mcrm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mcrm.listing', {
#             'root': '/mcrm/mcrm',
#             'objects': http.request.env['mcrm.mcrm'].search([]),
#         })

#     @http.route('/mcrm/mcrm/objects/<model("mcrm.mcrm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mcrm.object', {
#             'object': obj
#         })
