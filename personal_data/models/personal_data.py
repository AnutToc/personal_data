from odoo import models, fields

class PersonalData(models.Model):
    _name = 'personal.data'

    name = fields.Char(string="Name", required=True)
    picture = fields.Binary(string='Picture', attachment=True)
    birth_date = fields.Date(string="Birth Date", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone Number")
    website = fields.Char(string="Website")
    address = fields.Text(string="Address", required=True)
    job_position = fields.Char(string="Job Position", required=True)
    language = fields.Text(string="Languages", required=True)
    summary = fields.Text(string="Profile", required=True)

    experience_ids = fields.One2many(
        'personal.data.experience', 'personal_data_id', string="Experience", required=True
    )
    education_ids = fields.One2many(
        'personal.data.education', 'personal_data_id', string="Education", required=True
    )
    skill_ids = fields.One2many(
        'personal.data.skill', 'personal_data_id', string="Skills", required=True
    )
    award_ids = fields.One2many(
        'personal.data.certificate', 'personal_data_id', string="Awards & Certifications"
    )