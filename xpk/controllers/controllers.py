# -*- coding: utf-8 -*-
# from odoo import http


# class xpk(http.Controller):
#     @http.route('/xpk/xpk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xpk/xpk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xpk.listing', {
#             'root': '/xpk/xpk',
#             'objects': http.request.env['xpk.xpk'].search([]),
#         })

#     @http.route('/xpk/xpk/objects/<model("xpk.xpk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xpk.object', {
#             'object': obj
#         })
