# -*- coding: utf-8 -*-
import re
from datetime import datetime
from odoo import models, fields, api, exceptions


faculty_specialities_dict = {
	"Факультет інформатики": ["Інженерія програмного забезпечення", "Прикладна математика", "Комп\'ютерні науки", "Системний аналіз"],
	"Факультет правничих наук": [],
	"Факультет економічних наук": [],
	"Факультет природничих наук": [],
	"Факультет соціальних наук": [],
	"Факультет гуманітарних наук": [],
}


def get_faculties():
	return [(str(i), k) for i, k in enumerate(faculty_specialities_dict.keys())]


def get_specialities(faculty):
	specilities = faculty_specialities_dict.get(faculty)
	return [(str(i), k) for i, k in enumerate(specilities)]


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

	is_alumni = fields.Boolean(string='NaUKMA Alumni', default=False)
	show_alumni = fields.Boolean(string='Show alumni', default=False)

	diploma_naukma = fields.Boolean(string='Diploma NaUKMA', default=False)

	bachelor_degree = fields.Boolean(string='NaUKMA Bachelor', default=False)
	show_bachelor = fields.Boolean(string='Show bachelor', default=False)
	bachelor_faculty = fields.Selection(get_faculties(), string='Bachelor faculty')  # all faculties
	bachelor_speciality = fields.Selection(get_specialities("Факультет інформатики"), string='Bachelor speciality')  # temporary: only FI specialities
	bachelor_year_in = fields.Selection(get_years(), string='Bachelor entry year')
	bachelor_year_out = fields.Selection(get_years(), string='Bachelor finish year')

	master_degree = fields.Boolean(string='NaUKMA Master', default=False)
	show_master = fields.Boolean(string='Show master', default=False)
	master_faculty = fields.Char(string='Master faculty')
	master_speciality = fields.Char(string='Master speciality')
	master_year_in = fields.Selection(get_years(), string='Master entry year')
	master_year_out = fields.Selection(get_years(), string='Master finish year')

	@api.onchange('is_alumni')
	def alumni_checked(self):
		self.show_alumni = True if self.is_alumni else False

	@api.onchange('bachelor_degree')
	def _bachelor_checked(self):
		self.show_bachelor = True if self.bachelor_degree else False

	@api.onchange('master_degree')
	def _master_checked(self):
		self.show_master = True if self.master_degree else False

	@api.onchange('phone')
	def _check_phone_number(self):
		if self.phone:
			remove_odd_symbols_phone = re.sub("[^\+\d]", "", self.phone)
			if re.match("^\+\d{10,13}$", remove_odd_symbols_phone) is None:
				raise exceptions.ValidationError("Введіть телефонний номер в правильному форматі. Телефон повинен виглядати наступним чином +380444256064.")
			else:
				return {'value': {'phone': remove_odd_symbols_phone}}

	@api.onchange('mobile')
	def _check_mobile_number(self):
		if self.mobile:
			remove_odd_symbols_mobile = re.sub("[^\+\d]", "", self.mobile)
			if re.match("^\+\d{10,13}$", remove_odd_symbols_mobile) is None:
				raise exceptions.ValidationError("Введіть телефонний номер в правильному форматі. Телефон повинен виглядати наступним чином +380444256064.")
			else:
				return {'value': {'mobile': remove_odd_symbols_mobile}}
