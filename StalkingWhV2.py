#Sviluppato da Tommaso Patriti (-Ro0t) 


from selenium import webdriver
import time
import datetime
from sys import exit
import os

cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')

driver.get('http://web.whatsapp.com')



def usage():
	
	print("Usage: help\n")
	print("Options:")
	print("1      --Send automatically a message")
	print("2      --List of acces")
	options = input('Enter options:\n')
	if options=="1":
		automessage()
	if options=="2":
		stalkingacces()
	if options!="1"or"2":
		if options == "help":
			help()
		else:	
			print ("Please select a valid option!\n")
			time.sleep(2)
			usage()	


input('---Scan Qr code, then press enter---\n')


def automessage():
	name = input('Enter user or group name: ')
	msg = input('Enter message : ')
	count = int(input('Enter count : '))
	timesleep=input('Enter the time (in minutes) for the message to be sent: ')
	timesleep=int(timesleep)*60
	time.sleep(int(timesleep))
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_2bXVy')

	for i in range(count):
	    msg_box.send_keys(msg)
	    driver.find_element_by_class_name('_2lkdt').click()


def stalkingacces():
	name = input('Enter user name : ')
	online=0
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	time.sleep(5)


	try:
	    while True:
	    	try:
	    		acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
	    		if online==0:
	    			print(name,"Online at:", datetime.datetime.now())
	    			online=1

	    		
	    	except:
	    		if online==1:
	    			print(name,"Offline at:", datetime.datetime.now())
	    			print("---------------------------------------------------------")
	    			online=0
	except KeyboardInterrupt:
		print("Program quitted")
		exit(0)
		pass
def help():
	print("stolkingWh(beta-unstable)")
	print("Developed by Tommaso Patriti")
	print("No helps right now, retry in the next version! :)\n")
	time.sleep(3)
	usage()

usage()
