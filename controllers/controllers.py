# -*- coding: utf-8 -*-
from odoo import http

 class MyModule(http.Controller):
     @http.route('/al.account.balance',type='http', auth='public', website= True)
     return http.request.render('al.account.balance_page', {})

#     def index(self, **kw):
#         return ""

#     @http.route('/my_module/my_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_module/my_module',
#             'objects': http.request.env['my_module.my_module'].search([]),
#         })

#     @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module.object', {
#             'object': obj
#         })
