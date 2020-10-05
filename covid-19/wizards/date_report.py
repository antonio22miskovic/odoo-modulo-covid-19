# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import  api, fields, models, _
from odoo.exceptions import UserError

class DateReportWizard(models.TransientModel):
    _name = 'covid.wizard'
    _description = 'modal para fintrado por pais'

    start_date = fields.Date(
        string='Start Date',
        required=True,
    )

    end_date = fields.Date(
        string='End Date',
        required = True,
    )

    country_ids = fields.Many2many(
        'res.country',
        string='Countries',
        help='Generar reportes por pais', 
    )

    def print_report(self):
        covid19=self.env['covid.covid_19']
        domain=[
            ('datetime', '>', self.start_date),
            ('datetime','<', self.end_date)
        ]
        if self.country_ids:
            domain.append(('country_id','in',self.country_ids.ids))

        covidField=[
            'source',
            'datetime',
            'country_id',
            'infected',
            'recovered',
            'deseaced',
        ]
        covidRecords=covid19.search_read(domain,covidField)
        data={
            #~ 'doc_ids'
            'CovidRecords': covidRecords,
            'start date': self.start_date,
            'end date': self.end_date,
            'country_ids': self.country_ids,
        }

        return self.env.ref('covid-19.report_DateReportExternallayout').report_action(self, data=data)