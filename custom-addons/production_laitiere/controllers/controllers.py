# -*- coding: utf-8 -*-
# from odoo import http


# class ProductionLaitiere(http.Controller):
#     @http.route('/production_laitiere/production_laitiere', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/production_laitiere/production_laitiere/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('production_laitiere.listing', {
#             'root': '/production_laitiere/production_laitiere',
#             'objects': http.request.env['production_laitiere.production_laitiere'].search([]),
#         })

#     @http.route('/production_laitiere/production_laitiere/objects/<model("production_laitiere.production_laitiere"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('production_laitiere.object', {
#             'object': obj
#         })

