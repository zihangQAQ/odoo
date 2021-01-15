# -*- coding: utf-8 -*-
# from odoo import http


# class swdd(http.Controller):
#     @http.route('/swdd/swdd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/swdd/swdd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('swdd.listing', {
#             'root': '/swdd/swdd',
#             'objects': http.request.env['swdd.swdd'].search([]),
#         })

#     @http.route('/swdd/swdd/objects/<model("swdd.swdd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('swdd.object', {
#             'object': obj
#         })
