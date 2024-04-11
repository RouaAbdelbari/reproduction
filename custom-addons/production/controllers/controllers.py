# -*- coding: utf-8 -*-
# from odoo import http


# class Production(http.Controller):
#     @http.route('/production/production', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/production/production/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('production.listing', {
#             'root': '/production/production',
#             'objects': http.request.env['production.production'].search([]),
#         })

#     @http.route('/production/production/objects/<model("production.production"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('production.object', {
#             'object': obj
#         })

