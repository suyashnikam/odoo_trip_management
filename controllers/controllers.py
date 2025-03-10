# -*- coding: utf-8 -*-
# from odoo import http


# class TripManagement(http.Controller):
#     @http.route('/trip_management/trip_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trip_management/trip_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trip_management.listing', {
#             'root': '/trip_management/trip_management',
#             'objects': http.request.env['trip_management.trip_management'].search([]),
#         })

#     @http.route('/trip_management/trip_management/objects/<model("trip_management.trip_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trip_management.object', {
#             'object': obj
#         })

