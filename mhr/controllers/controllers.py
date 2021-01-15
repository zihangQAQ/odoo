# -*- coding: utf-8 -*-
# from odoo import http


# class mhr(http.Controller):
#     @http.route('/mhr/mhr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mhr/mhr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mhr.listing', {
#             'root': '/mhr/mhr',
#             'objects': http.request.env['mhr.mhr'].search([]),
#         })

#     @http.route('/mhr/mhr/objects/<model("mhr.mhr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mhr.object', {
#             'object': obj
#         })
