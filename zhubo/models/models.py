# -*- coding: utf-8 -*-

from odoo import models, fields, api


class zhubo(models.Model):
     _name = 'zhubo'
     _description = 'zhubo'

     name = fields.Char(string="主播", required=True)
     name2 = fields.Char(string="主播达人数字ID", required=True)
     name3 = fields.Char(string="运营主管花名")
     name4 = fields.Char(string="运营主管真实姓名", required=True)
     name5 = fields.Char(string="运营花名", required=True)
     name6 = fields.Char(string="当前负责运营同事", required=True)
     name7 = fields.Char(string="商务主管花名")
     name8 = fields.Char(string="商务主管真实姓名")
     name9 = fields.Char(string="商务花名")
     name10 = fields.Char(string="当前负责商务同事")
     name11 = fields.Char(string="买手主管")
     name12 = fields.Char(string="对接线下买手")
     name13 = fields.Char(string="推广位ID")
     name14 = fields.Char(string="主播招商链接")
     name15 = fields.Char(string="主播日常百元链接")
     name16 = fields.Char(string="金牌主播热门v任务链接")