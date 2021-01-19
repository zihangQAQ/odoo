# -*- coding: utf-8 -*-

from odoo import models, fields, api


class 商务订单(models.Model):
     _name = 'shangwudingdan'
     _description = 'shangwudingdan'

     name = fields.Char(string="v任务ID", required=True)
     priority = fields.Selection([('todo', '无'), ('normal', '有,未返点'), ('urgency', '有,已折扣')], default='todo', string='折扣/返点情况', required=True)
     test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
     priority2 = fields.Selection([('todo', '苏州集淘v后台'), ('normal', '苏州集淘支付宝'), ('urgency', '苏州集淘银行卡'), ('gear', '主播后台'), ('admit', '其他')], default='todo', string='原始进账方式', required=True)
     name2 = fields.Float(string="收款总金额")
     zhubobaojiamingxi = fields.Many2one('shangwudingdan1', string='主播报价明细')

# class 商务订单1(models.Model):
#      _name = 'shangwudingdan1'
#      _description = 'shangwudingdan'
#
#      name = fields.Char(string="123", required=True)
#      name2 = fields.Char(string="商家职位", required=True)
#      name3 = fields.Char(string="商家姓名")
#      name4 = fields.Char(string="联系手机号", required=True)
#      is_done = fields.Boolean(string="唯一客户主体信息", required=True)
#      is_done2 = fields.Boolean(string="是否有效客户")
#      priority = fields.Selection([('todo', '美妆护肤'), ('normal', '食品保健'), ('urgency', '服装搭配'), ('gear', '家具用品')], default='todo', string='客户类目', required=True)
#      test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
#      priority2 = fields.Selection([('todo', 'TP公司'), ('normal', '品牌方'), ('urgency', '公司分配'), ('gear', '独立开发'), ('admit', '前台接待'), ('expo', '线下展会'), ('cooperate', '以前合作过')], default='todo', string='客户来源', required=True)
#      name5 = fields.Char(string="原客户主题信息（自动）")
#      name6 = fields.Char(string="正确唯一客户主体信息（自动）")
#      priority3 = fields.Selection([('todo', '已检验'), ('normal', '未检验')], default='todo', string='是否唯一主体检验（自动）')
#      name7 = fields.Float(string="客户累计付款金额（自动）")



