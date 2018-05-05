#from .models import
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
#from .forms import
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Count
import os
import sys
from selenium import webdriver
import math
import time


def index(request):
    dinamic=0
    while dinamic<10:
        dinamic=dinamic+1



    cwd = os.getcwd()
    driver = webdriver.Chrome(cwd+'/chromedriver')
    driver.get('http://web.whatsapp.com')

    def qrCodeRead():
        time.sleep(1.5)
        qrCode = driver.find_element_by_class_name('_2EZ_m')
        qrCodeHtml=qrCode.get_attribute('innerHTML')
        return qrCodeHtml
    qrCodeRead()

    def stalkingacces():
    	name = input(Fore.GREEN + 'Enter user name : ')
    	online=0
    	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    	user.click()
    	time.sleep(5)
    	try:
    	    while True:
    	    	time.sleep(2)
    	    	try:
    	    		acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
    	    		if online==0:
    	    			onlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
    	    			online=1
    	    	except:
    	    		if online==1:
    	    			ofinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
    	    			online=0
    	except KeyboardInterrupt:
    		conn.close()



    #return ({'onlinedate':onlinedate, 'ofinedate':ofinedate})

    return render(request, 'index.html', {'qrCodeRead':qrCodeRead, 'dinamic':dinamic})
