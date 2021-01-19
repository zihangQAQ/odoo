# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class 商务订单(models.Model):
#      _name = 'shangwudingdan'
#      _description = 'shangwudingdan'
#
#      name = fields.Char(string="v任务ID", required=True)
#      priority = fields.Selection([('todo', '无'), ('normal', '有,未返点'), ('urgency', '有,已折扣')], default='todo', string='折扣/返点情况', required=True)
#      test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
#      priority2 = fields.Selection([('todo', '苏州集淘v后台'), ('normal', '苏州集淘支付宝'), ('urgency', '苏州集淘银行卡'), ('gear', '主播后台'), ('admit', '其他')], default='todo', string='原始进账方式', required=True)
#      name2 = fields.Float(string="收款总金额")


class 商务订单1(models.Model):
     _name = 'shangwudingdan1'
     _description = 'shangwudingdan1'

     name = fields.Char(string="主播名称", required=True)
     name2 = fields.Char(string="商务合作ID", required=True)
     priority = fields.Selection([('todo', '美妆'), ('normal', '非美妆')], default='todo', string='报价产品类别', required=True)
     test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
     name3 = fields.Float(string="单链接数/专场小时数")
     name4 = fields.Float(string="报价总金额")
     ceshi = fields.One2many('shangwudingdan','zhubobaojiamingxi',string = '测试')



