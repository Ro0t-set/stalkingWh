#!/usr/bin/env python

#Sviluppato da Tommaso Patriti (#Ro0t-set) 

import sqlite3
from selenium import webdriver
import time
import datetime
import os

cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')
driver.get('http://web.whatsapp.com')


def automessage():
	name = input('Enter user or group name: ')
	msg = input('Enter message : ')
	count = int(input('Enter count : '))
	timesleep=input('Enter the time (in minutes) for the message to be sent: ')
	timesleep=int(timesleep)*60
	time.sleep(int(timesleep))

	userSerch = driver.find_element_by_class_name('jN-F5 copyable-text selectable-text')
	userSerch.click()
	userSerch.send_keys(name)
	timesleep(2)


	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()


	msg_box = driver.find_element_by_class_name('_2bXVy')

	for i in range(count):
	    msg_box.send_keys(msg)
	    driver.find_element_by_class_name('_2lkdt').click()

automessage()