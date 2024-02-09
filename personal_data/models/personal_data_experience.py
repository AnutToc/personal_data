from odoo import models, fields

class PersonalDataExperience(models.Model):
    _name = 'personal.data.experience'

    personal_data_id = fields.Many2one('personal.data', string="Personal Data")
    company_name = fields.Char(string="Company Name")
    job_title = fields.Char(string="Job Title")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    responsibilities = fields.Text(string="Responsibilities")
    achievements = fields.Text(string="Achievements")