# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Anchor_sales_data(models.Model):
    _name = 'anchor.sales_data'
    _description = '主播销售数据'

    Live_ID = fields.Char(string='直播ID')
    name = fields.Many2one('anchor.information',string='主播名')
    date = fields.Date(string='日期')