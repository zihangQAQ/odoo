# -*- coding: utf-8 -*-
# from odoo import http


# class mhr(http.Controller):
#     @http.route('/zhubo/zhubo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zhubo/zhubo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mhr.listing', {
#             'root': '/zhubo/zhubo',
#             'objects': http.request.env['zhubo.zhubo'].search([]),
#         })

#     @http.route('/zhubo/zhubo/objects/<model("zhubo.zhubo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zhubo.object', {
#             'object': obj
#         })
