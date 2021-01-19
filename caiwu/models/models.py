# -*- coding: utf-8 -*-

from odoo import models, fields, api


class 财务(models.Model):
     _name = 'cw'
     _description = 'cw'

     name = fields.Char(string="商务同事花名", required=True)
     name2 = fields.Char(string="商务ID", required=True)
     name3 = fields.Char(string="所属部门")
     name4 = fields.Char(string="发票申请人", required=True)
     name5 = fields.Char(string="冲红")
     name6 = fields.Char(string="发票号码")
     name7 = fields.Char(string="单位名称")
     name8 = fields.Char(string="发票税号")
     name9 = fields.Char(string="发票类型")
     name10 = fields.Float(string="发票含税金额")
     test_time = fields.Datetime(string="开票日期", default=fields.Datetime.now)
     name11 = fields.Char(string="快递单号")
     flighttime = fields.Binary(string="快递照片")
     flighttime1 = fields.Binary(string="快递面单")
     name12 = fields.Float(string="快递费用")
     test_time1 = fields.Datetime(string="取件日期", default=fields.Datetime.now)
     is_done = fields.Boolean(string="是否登记v任务与钉钉流程", required=True)
     test_time2 = fields.Datetime(string="发票申请日期", default=fields.Datetime.now)
     name13 = fields.Char(string="钉钉审批编号")
     name14 = fields.Char(string="修正原因")
     name15 = fields.Float(string="钉钉申请含税金额")
     name16 = fields.Float(string="修正含税金额")


class 财务1(models.Model):
     _name = 'cw1'
     _description = 'cw'

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



