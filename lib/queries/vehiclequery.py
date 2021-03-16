#!/usr/bin/python3
#-*- coding:utf-8 -*-

from .interface import Requester 
from .entities.user import UserInfo

class PatentQuery(Requester):
	def __init__(self, driver):
		self.driver = driver


	def interactive(self):
		raise NotImplementedError


	def get_table(self):
		raise NotImplementedError


	def __del__(self):
		self.driver.quit()	


