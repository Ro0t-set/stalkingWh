#Sviluppato da Tommaso Patriti (-Ro0t) 


from selenium import webdriver
import time
import datetime
import sys
import os

cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')

driver.get('http://web.whatsapp.com')



def usage():
	print("Usage: stolkingWh <options>\n")
	print("Options:")
	print("1        send automatically a message")
	print("2        list of acces")
	options = input('Enter options:')
	if options=="1":
		automessage()
	if options=="2":
		stalkingacces()


input('Enter anything after scanning QR code')


def automessage():
	name = input('Enter the name of user or group : ')
	msg = input('Enter the message : ')
	count = int(input('Enter the count : '))
	timesleep=input('Enter the time in minutes after which you want the message to be sent (0 to istant): ')
	timesleep=int(timesleep)*60
	time.sleep(int(timesleep))
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_2bXVy')

	for i in range(count):
	    msg_box.send_keys(msg)
	    driver.find_element_by_class_name('_2lkdt').click()


def stalkingacces():
	name = input('Enter the name of user : ')
	online=0
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	time.sleep(5)


	try:
	    while True:
	    	time.sleep(1)
	    	try:
	    		acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
	    		if online==0:
	    			print(name,"è online alle", datetime.datetime.now())
	    			online=1		
	    	except:
	    		if online==1:
	    			print(name,"è ofline alle", datetime.datetime.now())
	    			print("------------------------------------------------------------------")
	    			online=0
	except KeyboardInterrupt:
		sys.exit('Program quitted')
		pass

usage()
