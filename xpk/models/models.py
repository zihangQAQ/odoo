# -*- coding: utf-8 -*-

from odoo import models, fields, api


class 选品库(models.Model):
     _name = 'xuanpinku'
     _description = 'xuanpinku'

     name = fields.Char(string="对接人花名", required=True)
     name2 = fields.Char(string="费用/纯佣", required=True)
     name3 = fields.Char(string="商家需求")
     name4 = fields.Char(string="产品名", required=True)
     name5 = fields.Char(string="产品链接", required=True)
     name6 = fields.Char(string="产品卖点")
     name7 = fields.Char(string="规格")
     name8 = fields.Char(string="日常零售价")
     name9 = fields.Char(string="直播间到手价")
     name10 = fields.Char(string="历史最低价")
     name11 = fields.Char(string="优惠方式")
     name12 = fields.Char(string="佣金比率")
     name13 = fields.Char(string="定向佣金链接")
     name14 = fields.Char(string="商品ID")
     name15 = fields.Char(string="主播名")
     name16 = fields.Char(string="对接商务真实姓名")
     name17 = fields.Char(string="播出日期")
     name18 = fields.Char(string="v任务ID")
     name19 = fields.Char(string="退款金额")
     name20 = fields.Char(string="掌柜旺旺")
     name21 = fields.Char(string="主播百元链接")
     name22 = fields.Char(string="主播达人数字ID")
     name23 = fields.Char(string="主播后台v任务ID")
     is_done = fields.Boolean(string="是否拍v")
     name24 = fields.Float(string="计算收费金额")
     test_time = fields.Datetime(string="填写日期", default=fields.Datetime.now)






class 选品库1(models.Model):
     _name = 'xuanpinchi'
     _description = 'xuanpinku'

     name = fields.Char(string="123", required=True)
     name2 = fields.Char(string="商家职位", required=True)
     name3 = fields.Char(string="商家姓名")
     name4 = fields.Char(string="联系手机号", required=True)
     is_done = fields.Boolean(string="唯一客户主体信息", required=True)
     is_done2 = fields.Boolean(string="是否有效客户")
     priority = fields.Selection([('todo', '美妆护肤'), ('normal', '食品保健'), ('urgency', '服装搭配'), ('gear', '家具用品')], default='todo', string='客户类目', required=True)
     test_time = fields.Datetime(string="首次登记日期", default=fields.Datetime.now)
     priority2 = fields.Selection([('todo', 'TP公司'), ('normal', '品牌方'), ('urgency', '公司分配'), ('gear', '独立开发'), ('admit', '前台接待'), ('expo', '线下展会'), ('cooperate', '以前合作过')], default='todo', string='客户来源', required=True)
     name5 = fields.Char(string="原客户主题信息（自动）")
     name6 = fields.Char(string="正确唯一客户主体信息（自动）")
     priority3 = fields.Selection([('todo', '已检验'), ('normal', '未检验')], default='todo', string='是否唯一主体检验（自动）')
     name7 = fields.Float(string="客户累计付款金额（自动）")



