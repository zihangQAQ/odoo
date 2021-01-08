# -*- coding: utf-8 -*-

from odoo import models, fields, api






class Operation_team(models.Model):
    _name = 'operation.team'
    _description = '运营团队'

    Team_name = fields.Char(stirng='团队名称')
    Team_leader = fields.Char(string='团队主管')
    Deputy_Team_leader = fields.Char(string='团队副主管')
    personnel_name = fields.Char(string='人员姓名')
