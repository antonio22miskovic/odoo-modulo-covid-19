# -*- coding: utf-8 -*-

from odoo import models, fields, api

class covid_19(models.Model):
    _name = 'covid.covid_19'

    source 			= fields.Char(string='Source',required=True)
    datetime 		= fields.Datetime(string='Date Time',required=True, default=fields.Datetime.now())
    country_id 		= fields.Many2one('res.country',required=True)
    infected 		= fields.Integer(string='infected',required=True, default=0)
    recovered 		= fields.Integer(string='recovered',required=True, default=0)
    deseaced 		= fields.Integer(string='deseaced',required=True, default=0)
    total_infected  = fields.Integer(string='Total Infected', compute='set_total_infected', required=True, default=0)
    total_recovered = fields.Integer(string='Total Recovered', compute='set_total_recovered', required=True, default=0)
    total_deseaced  = fields.Integer(string='Total Deseaced', compute='set_total_deseaced', required=True, default=0)


    description = fields.Text()	

    def set_total_infected(self): #total de infectados
    	for data in self:
    		domain=[
    			('country_id','=',data.country_id.id),
    			('datetime', '<', data.datetime)	
    		]
    		records=self.search(domain)
    		Infecteds=records.mapped('infected')
    		data.total_infected=sum(Infecteds)+data.infected


    def set_total_recovered(self): #total de recuperados 
    	for data in self:
    		domain=[
    			('country_id','=',data.country_id.id),
    			('datetime','<',data.datetime) 
    		]
    		records=self.search(domain)
    		Recovered=records.mapped('recovered')
    		data.total_recovered=sum(Recovered)+data.recovered


    def set_total_deseaced(self): # total de fallecidos 
    	for data in self:
    		domain=[
    			('country_id','=',data.country_id.id),
    			('datetime','<',data.datetime) 
    		]
    		records=self.search(domain)
    		Deseaced=records.mapped('deseaced')
    		data.total_deseaced=sum(Deseaced)+data.deseaced

    def set_percentage_infected(self):
        total=0
        if self.infected:
            total=(self.infected*100)/self.total_infected
        return total
      
    def set_percentage_recovered(self):
        total=0
        if self.recovered:
            total=(self.recovered*100)/self.total_recovered
        return total 
      
    def set_percentage_deseaced(self):
        total=0
        if self.deseaced:
            total=(self.deseaced*100)/self.total_deseaced
        return total