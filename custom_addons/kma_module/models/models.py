# -*- coding: utf-8 -*-
import re
from datetime import datetime
from odoo import models, fields, api, exceptions


def get_years():
	year_list = []
	for i in range(1991, datetime.today().year + 10):
		year_list.append((str(i), str(i)))
	return year_list


class AlumniContact(models.Model):
	_inherit = 'res.partner'
	
	full_name = fields.Char(string='Full name')
	birth_date = fields.Date(string='Date of birth')

	facebook_link = fields.Char(string='Facebook')
	linkedin_link = fields.Char(string='LinkedIn')
	skype = fields.Char(string='Skype')
	telegram = fields.Char(string='Telegram')
	viber = fields.Char(string='Viber')

	diploma_naukma = fields.Boolean(string='Diploma NaUKMA', default=False)

	bachelor_degree = fields.Boolean(string='NaUKMA Bachelor', default=False)
	show_bachelor = fields.Boolean(string='Show bachelor', default=False)
	bachelor_faculty = fields.Char(string='Bachelor faculty')
	bachelor_speciality = fields.Char(string='Bachelor speciality')
	bachelor_year_in = fields.Selection(get_years(), string='Entry year')
	bachelor_year_out = fields.Selection(get_years(), string='Finish year')

	master_degree = fields.Boolean(string='NaUKMA Master', default=False)
	show_master = fields.Boolean(string='Show master', default=False)
	master_faculty = fields.Char(string='Bachelor faculty')
	master_speciality = fields.Char(string='Master speciality')
	master_year_in = fields.Selection(get_years(), string='Entry year')
	master_year_out = fields.Selection(get_years(), string='Finish year')

	@api.onchange('master_degree')
	def _master_checked(self):
		self.show_master = True if self.master_degree else False

	@api.onchange('bachelor_degree')
	def _bachelor_checked(self):
		if self.bachelor_degree:
			self.show_bachelor = True
		else:
			self.show_bachelor = False

	@api.constrains('phone')
	def _check_phone_number(self):
		if re.match("^\+\d{10,13}$", self.phone) is None:
			raise exceptions.ValidationError("Введіть телефонний номер в правильному форматі. Телефон повинен виглядати наступним чином +380444256064.")
