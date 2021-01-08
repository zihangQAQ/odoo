# -*- coding: utf-8 -*-
# from odoo import http


# class 子航(http.Controller):
#     @http.route('/子航/子航/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/子航/子航/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('子航.listing', {
#             'root': '/子航/子航',
#             'objects': http.request.env['子航.子航'].search([]),
#         })

#     @http.route('/子航/子航/objects/<model("子航.子航"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('子航.object', {
#             'object': obj
#         })
