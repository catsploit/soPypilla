#!/usr/bin/python3
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from .interface import Requester
from .entities.user import UserInfo



class PageQuery(Requester):
	def __init__(self, driver):
		self.driver = driver


	def interactive(self, user):
		self.driver.get('https://www.nombrerutyfirma.com')
		is_rut = self.is_rut(user)

		if is_rut:
			holder = 'Buscar por RUT'
			self.detect('//*[contains(text(),"RUT")]').click()

		else:
			holder = 'Buscar por Nombre y Apellido de una persona'

		field = self.detect(f'//input[@placeholder="{holder}"]')
		field.send_keys(f'{user}', Keys.RETURN)
		
		# Wait until results table is loaded
		return self.wait().get_attribute('innerHTML')


	def get_table(self, source):
		soup = BeautifulSoup(source, 'html.parser')
		table = soup.find('tbody')
		results = {}

		lines = table.find_all('tr')
		for line in lines:
			fields = line.find_all('td')
			fields = [f.text.strip() for f in fields]

			results[fields[1]] = UserInfo(
									direction = fields[3],
									city = fields[4],
									name = fields[0],
									rut = fields[1],
									sex = fields[2])

		return results
		

	def __del__(self):
		self.driver.quit()