#!/usr/bin/python3
#-*- coding:utf-8 -*-

from selenium import webdriver
from lib.queries.userquery import PageQuery

# Note: you can use almost any driver
# but I'm using Firefox this time
driver = webdriver.Firefox()
user = PageQuery(driver)


# add 'to_dict=True' as a param if you want
# to do some fancy json conversions
print(user.search('nicolas gonzales'))