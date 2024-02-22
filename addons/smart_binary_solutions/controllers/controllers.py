# -*- coding: utf-8 -*-
# from odoo import http


# class SmartBinarySolutions(http.Controller):
#     @http.route('/smart_binary_solutions/smart_binary_solutions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_binary_solutions/smart_binary_solutions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_binary_solutions.listing', {
#             'root': '/smart_binary_solutions/smart_binary_solutions',
#             'objects': http.request.env['smart_binary_solutions.smart_binary_solutions'].search([]),
#         })

#     @http.route('/smart_binary_solutions/smart_binary_solutions/objects/<model("smart_binary_solutions.smart_binary_solutions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_binary_solutions.object', {
#             'object': obj
#         })
