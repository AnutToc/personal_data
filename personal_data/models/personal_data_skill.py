from odoo import models, fields

class PersonalDataSkill(models.Model):
    _name = 'personal.data.skill'

    personal_data_id = fields.Many2one('personal.data', string="Personal Data")
    skill = fields.Char(string="Skill")