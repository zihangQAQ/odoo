# -*- coding: utf-8 -*-

from odoo import models, fields, api






class Anchor_information(models.Model):
    _name = 'anchor.information'
    _description = '主播信息'

    name = fields.Char(string='主播名')
    Operation_name = fields.Char(string='运营姓名')
    Operation_team = fields.Char(string='运营团队')
    Join_time = fields.Date(srting='加入时间')
    Anchor_scheduling = fields.Char(string='主播排期')