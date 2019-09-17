# -*- coding: utf-8 -*-

from odoo import models, fields, api

class marketplace_module(models.Model):
     _name = 'al.account.balance'

     CurrencyBalance_ID = fields.Integer(string='CurrencyBalance ID')
     Student_ID = fields.Many2one('op.student', string 'Student ID')
     Current_Balance = fields.Integer(string='Current Balance')
     Faculty_ID = fields.Many2one('op.faculty', string='Faculty ID')
     Transaction_ID = fields.Many2one('al.transaction.lines' string)='Transaction ID')
     
