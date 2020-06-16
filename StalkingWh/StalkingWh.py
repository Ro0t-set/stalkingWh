#!/usr/bin/env python

#Sviluppato da Tommaso Patriti (#Ro0t-set) 

import sqlite3
from selenium import webdriver
import time
import datetime
from sys import exit
from colorama import init
from colorama import Fore, Back, Style
import os
from acces import Acces
init()
cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')
conn = sqlite3.connect('acces.db')
c = conn.cursor()
driver.get('http://web.whatsapp.com')



def usage():
	
	print(Fore.RED + "Usage: help\n") 
	print(Style.RESET_ALL)
	print(Fore.YELLOW + "Options:")
	print("1      --Send automatically a message")
	print("2      --List of acces")
	options = input('Enter options:\n')

	if options=="1":
		automessage()
	elif options=="2":
		stalkingacces()
	elif options=="3":
		stalkingall()
	if options!="1"or"2"or"3":
		if options == "help":
			help()
		else:	
			print(Style.RESET_ALL)
			print(Back.RED + "Please select a valid option!")
			print(Style.RESET_ALL)
			time.sleep(2)
			os.system('clear')
			usage()	

print(Style.RESET_ALL)
input(Fore.RED + '---Scan Qr code, then press enter---\n')


def automessage():
	name = input('Enter user or group name: ')
	msg = input('Enter message : ')
	count = int(input('Enter count : '))
	timesleep=input('Enter the time (in minutes) for the message to be sent: ')
	timesleep=int(timesleep)*60
	time.sleep(int(timesleep))

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	time.sleep(2)

	msg_box =  driver.find_element_by_class_name('_3uMse')

	for i in range(count):
	    msg_box.send_keys(msg)
	    driver.find_element_by_class_name('_1U1xa').click()


def stalkingacces():

	online=0
	name =input("name (to write db): ")
	print("click on chat")
	try:
	    while True:
	    	time.sleep(2)
	    	try:
	    		acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
	    		if online==0:
	    			onlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
	    			complilation=Acces(name,1,onlinedate)
	    			c.execute("INSERT INTO acces VALUES('{}', '{}', '{}')".format(complilation.name, complilation.state, complilation.accesdate))
	    			conn.commit()

	    			print(name)
	    			print(Style.RESET_ALL)
	    			print(Fore.GREEN + name,"Online at:", datetime.datetime.now().strftime("%y-%m-%d, %H:%M"))
	    			online=1

	    		
	    	except:
	    		if online==1:
	    			onlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
	    			complilation=Acces(name,0,onlinedate)
	    			c.execute("INSERT INTO acces VALUES('{}', '{}', '{}')".format(complilation.name, complilation.state, complilation.accesdate))
	    			conn.commit()



	    			print(name,"Offline at:", datetime.datetime.now().strftime("%y-%m-%d, %H:%M"))
	    			print("---------------------------------------------------------")
	    			online=0
	except KeyboardInterrupt:
		deinit()
		conn.close()
		print("Program quitted")
		exit(0)
		pass





		
		
def help():
	print(Fore.RED + "stolkingWh(beta-unstable)")
	print("Developed by Tommaso Patriti")
	print("No helps right now, retry in the next version! :)\n")
	time.sleep(1)
	usage()

usage()
