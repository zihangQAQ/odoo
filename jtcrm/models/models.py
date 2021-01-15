# -*- coding: utf-8 -*-

from odoo import models, fields, api

#引起一下报错，注释掉后再重新启动
#Internal Server Error
#The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
class TodoCategory(models.Model):
    _name = 'crm.category'
    _description = '客户类目'

    name = fields.Char(string="客户类目",required=True)
    crm_ids = fields.One2many("crm.task","category_id",string="客户类目")
    crm_count =fields.Integer(string="数量", compute="_compute_task_count")

    @api.depends("crm_ids")
    @api.model
    def _compute_task_count(self):
        for rec in self:
            rec.crm_count = len(rec.crm_ids)




class TodoTask(models.Model):
    _name = 'crm.task'
    _description = 'crm.todo'

    name = fields.Char(string = "客户名称")
    is_done = fields.Boolean(string = "是否完成")
    priority = fields.Selection([('todo','待办'),('normal','普通'),('urgency','紧急')],default = 'todo',string = '紧急程度')
    deadline = fields.Datetime(string = "截止时间")
    is_expired = fields.Boolean(string = "是否过期",compute = "_compute_is_expired")
    category_id = fields.Many2one("crm.category",string ="类别")
    color = fields.Integer()



    @api.depends("deadline")
    @api.model
    def _compute_is_expired(self):
        for rec in self:
            if rec.deadline:
                rec.is_expired = rec.deadline < fields.Datetime.now()
            else:
                rec.is_expired =False

