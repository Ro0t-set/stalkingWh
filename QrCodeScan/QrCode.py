from selenium import webdriver
import time
import os

cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')
driver.get('http://web.whatsapp.com')

def get_qrcode():

	qrCode = driver.find_element_by_class_name('_2EZ_m')
	qrCodeHtml=qrCode.get_attribute('innerHTML')
	print(qrCodeHtml)
	return (qrCodeHtml)

get_qrcode()