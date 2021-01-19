# -*- coding: utf-8 -*-
# from odoo import http


# class caiwu(http.Controller):
#     @http.route('/caiwu/caiwu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caiwu/caiwu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caiwu.listing', {
#             'root': '/caiwu/caiwu',
#             'objects': http.request.env['caiwu.caiwu'].search([]),
#         })

#     @http.route('/caiwu/caiwu/objects/<model("caiwu.caiwu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caiwu.object', {
#             'object': obj
#         })
