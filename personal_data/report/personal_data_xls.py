from odoo import api, models
import io
import base64

class ResumeExportExcel(models.AbstractModel):
    _name = 'report.personal_data.report_personal_data_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, records):
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:H', 50)
        text_center_format = workbook.add_format({'align': 'center', 'border':2, 'border_color':'cyan', 'bg_color': 'cyan'})
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'font_name': 'Arial', 'font_size': 14, 'font_color': 'white', 'bg_color': 'blue'})
        body_format = workbook.add_format({'align': 'vjustify', 'font_name': 'Calibri', 'font_size': 11, 'border':2, 'border_color':'cyan', 'bg_color': '#ADD8E6'})
        
        for record in records:
            # Profile Section
            picture = io.BytesIO(base64.b64decode(record.picture))
            worksheet.write('A1', record.name, header_format)
            worksheet.write('A2', record.job_position, text_center_format)
            worksheet.insert_image('B1', "image.png", {'x_offset': 125, 'y_offset': 10, 'x_scale': 1, 'y_scale': 0.5, 'image_data': picture})
            worksheet.write('A4', 'Profile', header_format)
            worksheet.write('A5', record.summary, body_format)

            # Experience Section
            worksheet.write('A7', 'Experience', header_format)
            row = 7
            col = 0
            for experience in record.experience_ids:
                worksheet.write(row, col, experience.company_name, text_center_format)
                worksheet.write(row + 1, col, experience.job_title, text_center_format)
                worksheet.write(row + 2, col, (experience.start_date.strftime('%b %Y') + ' - ' + experience.end_date.strftime('%b %Y')), text_center_format)
                worksheet.write(row + 3, col, experience.responsibilities, body_format)
                col += 1

            # Skills Section
            worksheet.write('A13', 'Skills', header_format)
            row = 13
            for skill in record.skill_ids:
                worksheet.write(row, 0, skill.skill, text_center_format)
                row += 1

            # Languages Section
            worksheet.write('B13', 'Languages', header_format)
            languages = record.language.splitlines()
            languages_string = ', '.join(languages[:-1])  # Join all languages except the last one with commas
            languages_string += ' and ' + languages[-1]  # Add the last language with "and"
            worksheet.write('B14', languages_string, text_center_format)

            # Contact Section
            worksheet.write('B15', 'Contact', header_format)
            worksheet.write('B16', record.email, text_center_format)
            worksheet.write('B17', record.phone, text_center_format)
            if record.website:
                worksheet.write('B18', record.website, text_center_format)

            # Awards Section
            row += 1
            worksheet.write(row, 0, 'Awards and Certifications', header_format)
            row += 1
            for award in record.award_ids:
                worksheet.write(row, 0, award.institution, body_format)
                worksheet.write(row, 1, award.title, body_format)
                row += 1

            # Education Section
            row += 1
            worksheet.write(row, 0, 'Education', header_format)
            row += 1
            for education in record.education_ids:
                worksheet.write(row, 0, education.institution, text_center_format)
                worksheet.write(row, 1, (education.degree + ' ' + education.major), text_center_format)
                row += 1
    