# -*- coding: utf-8 -*-
from odoo import http

# class KmaModule(http.Controller):
#     @http.route('/kma_module/kma_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kma_module/kma_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kma_module.listing', {
#             'root': '/kma_module/kma_module',
#             'objects': http.request.env['kma_module.kma_module'].search([]),
#         })

#     @http.route('/kma_module/kma_module/objects/<model("kma_module.kma_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kma_module.object', {
#             'object': obj
#         })