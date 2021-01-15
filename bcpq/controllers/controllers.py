# -*- coding: utf-8 -*-
# from odoo import http


# class bcpq(http.Controller):
#     @http.route('/bcpq/bcpq/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bcpq/bcpq/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bcpq.listing', {
#             'root': '/bcpq/bcpq',
#             'objects': http.request.env['bcpq.bcpq'].search([]),
#         })

#     @http.route('/bcpq/bcpq/objects/<model("bcpq.bcpq"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bcpq.object', {
#             'object': obj
#         })
