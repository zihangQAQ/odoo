
# -*- coding: utf-8 -*-

from odoo import models, fields, api







class ycrm(models.Model):
    _name = 'ycrm.crm'
    _description = 'crm'

    name = fields.Char(string="v任务ID", required=True)
    name2 = fields.Char(string="店铺名称", required=True)
    name3 = fields.Char(string="主播名")
    name4 = fields.Float(string="金额", required=True)
    test_time = fields.Datetime(string="播出日期", default=fields.Datetime.now)
    name5 = fields.Float(string="退款金额", required=True)
    name6 = fields.Char(string="商务合作ID")
    name7 = fields.Char(string="订单对接人")