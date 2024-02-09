from odoo import models, fields

class PersonalDataCertificate(models.Model):
    _name = 'personal.data.certificate'

    personal_data_id = fields.Many2one('personal.data', string="Personal Data")
    institution = fields.Char(string="Institution")
    title = fields.Char(string="Title")
    date = fields.Date(string="Date")