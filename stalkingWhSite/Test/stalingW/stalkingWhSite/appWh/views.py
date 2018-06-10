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
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
import os
import sys
from selenium import webdriver
import math
import time
import random
from django.template.context_processors import csrf

def drivers():
    cwd = os.getcwd()
    driver = webdriver.Chrome(cwd+'/chromedriver')
    driver.get('http://web.whatsapp.com')
    return driver



def qrCodeRead(request):
    driver= drivers()
    a=0
    while a<20:
        try:
            qrCode = driver.find_element_by_class_name('_2EZ_m')
            qrCodeHtml=qrCode.get_attribute('innerHTML')
            a=20
        except:
            time.sleep(1)
            a=a+1

    return render(request, 'QRcode.html', {'qrCodeHtml':qrCodeHtml, 'driver':driver})



def serchName(drivers):
    drivers= driver
    name= "Antonio Elettronico"
    a=0
    while a<20:
        try:
            userSerch = driver.find_element_by_class_name('jN-F5')
            userSerch.click()
            userSerch.send_keys(name)
            a=20
        except:
            time.sleep(1)
            a=a+1




def index(request, drivers):
    drivers= driver
    serchName()

    c = {}
    c.update(csrf(request))

    def stalkingacces():
        try:
            acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
            statedate=datetime.datetime.now().strftime("online: %y-%m-%d, %H:%M")
            print("online")
            return(statedate)
        except:
                statedate=datetime.datetime.now().strftime("offline: %y-%m-%d, %H:%M")
                print("ofline")
                return(statedate)
    StalkingAcces=stalkingacces()

    if request.method == 'POST':

        print("success!!")
        time.sleep(3)
        return HttpResponse(
            json.dumps(StalkingAcces),
            c
        )

    return render(request, 'index.html', {'stalkingacces': stalkingacces,}, c)

    # cwd = os.getcwd()
    # driver = webdriver.Chrome(cwd+'/chromedriver')
    # driver.get('http://web.whatsapp.com')
    # if request.method == 'POST':
    #     def qrCodeRead():
    #         time.sleep(5)
    #         qrCode = driver.find_element_by_class_name('_2EZ_m')
    #         qrCodeHtml=qrCode.get_attribute('innerHTML')
    #         return qrCodeHtml
    #
    #     read = qrCodeRead()
    #     return render(request, 'index.html', {'qrCodeRead': read})
    # else:
    #     cwd = os.getcwd()
    #     driver = webdriver.Chrome(cwd+'/chromedriver')
    #     driver.get('http://web.whatsapp.com')
    #
    #     #offlinedate = ""
    #     #onlinedate = ""
    #

        #def nameStalingAcces():
            #time.sleep(10)
            #name = "Tommaso Patriti"
            #online=0
            #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            #user.click()

        #nameStalingAcces()

        #def stalkingacces():
            #try:
                #acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
                #if online==0:
                    #onlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
                    #online=1
            #except:
                #if online==1:
                    #offlinedate=datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
                    #online=0
