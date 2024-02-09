from odoo import models, fields

class PersonalDataEducation(models.Model):
    _name = 'personal.data.education'

    personal_data_id = fields.Many2one('personal.data', string="Personal Data")
    institution = fields.Char(string="Institution")
    degree = fields.Char(string="Degree")
    major = fields.Char(string="Major")
    graduation_year = fields.Date(string="Graduation Year")