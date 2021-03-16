#!/usr/bin/python3
#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from re import sub
from typing import Dict, Any


class Requester:
	def interactive(self, user : str) -> str:
		"""Interact with page and returns driver source code
		
		Args:
			user (str): user id, name, to search

		Returns:
			self.driver.page_source (str): source code after searching
		"""
		raise NotImplementedError


	def get_table(self, source : str) -> Dict[str, Any]:
		"""Read html and returns table in dictionary
		
		Args:
			source (str): HTML code from Selenium driver

		Returns
			dict: a dictionary with (rut : attributes) format
		"""
		raise NotImplementedError


	def detect(self, expression) -> Any:
		return self.driver.find_elements(By.XPATH, expression)[0]
	

	def wait(self) -> Any:
		stay = WebDriverWait(self.driver, 10)
		return stay.until(EC.presence_of_element_located((By.TAG_NAME, 'table'))) #old: thead


	def is_rut(self, user : str) -> bool:
		if sub('[ .-]', '', user).isnumeric():
			return True
		return False

		
	def search(self, user : str, to_dict: bool = False) -> Dict[str, Any]:
		result = self.get_table(self.interactive(user))
		if to_dict:
			for usr in result:
				result[usr] = vars(result[usr])

		return result