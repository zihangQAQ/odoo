# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class 子航(models.Model):
#     _name = '子航.子航'
#     _description = '子航.子航'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class zhubofenlei(models.Model):
    _name = "zhubo.fenlei"
    _description = '主播分类'

    name = fields.Char(string = '主播类别',required = True)

class 子航(models.Model):
    _name = 'zhubo.xiaoshoushuju'
    _auto = True
    name = fields.Char(string = '主播名')
    date = fields.Date(string = '日期')
    xiaoshoue = fields.Char(string = '销售额')
    name1 = fields.Many2one("crm", string='类别')
    name2 = fields.Many2one("crm", string='产品类目')

# class Anchor_sales_data(models.Model):
#     _name = 'Anchor.sales_data'
#     _description = '主播销售数据'
#
#     Live_ID = fields.Many2one('Anchor.information',string='直播ID')
#     name = fields.Many2one('Anchor.information',string='主播名')
#     date = fields.Date(string='日期')
# class Anchor_information(models.Model):
#     _name = 'Anchor.information'
#     _description = '主播信息'
#
#     name = fields.Char(string='主播名')
#     Operation_name = fields.Char(string='运营姓名')
#     Operation_team = fields.Char(string='运营团队')
#     Join_time = fields.Date(srting='加入时间')
#     Anchor_scheduling = fields.Char(string='主播排期')
#
# class Operation_team(models.Model):
#     _name = 'operation.team'
#     _description = '运营团队'
#
#     Team_name = fields.Char(stirng='团队名称')
#     Team_leader = fields.Char(string='团队主管')
#     Deputy_Team_leader = fields.Char(string='团队副主管')
#     personnel_name = fields.Char(string='人员姓名')
