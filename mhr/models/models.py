# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mhr(models.Model):
     _name = 'mhr'
     _description = 'crm'

     name = fields.Char(string="花名", required=True)
     name2 = fields.Char(string="真实姓名", required=True)
     name3 = fields.Char(string="职务")
     name4 = fields.Char(string="商务ID", required=True)
     name5 = fields.Char(string="所属部门", required=True)
     name6 = fields.Char(string="直属领导", required=True)
     name7 = fields.Char(string="在职状态", required=True)
     name8 = fields.Char(string="联系手机号", required=True)
     name9 = fields.Char(string="微信号", required=True)
     name10 = fields.Char(string="工作邮箱")
     priority = fields.Selection([('todo', '美妆护肤'), ('normal', '食品保健'), ('urgency', '服饰搭配/珠宝/鞋包/饰品'), ('gear', '家居用品/数码/家电' )], default='todo', string='垂直类目')
     name11 = fields.Char(string="分配客户数")
     is_done = fields.Boolean(string="是否接单")
     name12 = fields.Char(string="v任务接单链接")
     test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
     name13 = fields.Char(string="3月提成方案")
     name14 = fields.Char(string="4月提成方案")
     name15 = fields.Char(string="5月提成方案")
     name16 = fields.Char(string="6月提成方案")
     name17 = fields.Char(string="7月提成方案")
     name18 = fields.Char(string="8月提成方案")