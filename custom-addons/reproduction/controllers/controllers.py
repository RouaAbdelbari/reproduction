# -*- coding: utf-8 -*-
# from odoo import http


# class Reproduction(http.Controller):
#     @http.route('/reproduction/reproduction', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reproduction/reproduction/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reproduction.listing', {
#             'root': '/reproduction/reproduction',
#             'objects': http.request.env['reproduction.reproduction'].search([]),
#         })

#     @http.route('/reproduction/reproduction/objects/<model("reproduction.reproduction"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reproduction.object', {
#             'object': obj
#         })

