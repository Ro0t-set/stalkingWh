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
cwd = os.getcwd()
driver = webdriver.Chrome(cwd+'/chromedriver')
driver.get('http://web.whatsapp.com')


def stalk(request):
    if request.method == 'GET':
        return render(request, 'stalk.html')
    else:
        return JsonResponse({'data': 'foo'})

def index(request):

    c = {}
    c.update(csrf(request))
     # ... view code here

    def stalkingacces():

        try:
            if online==0:
                print("2")
        except:
            online=0

        try:
            acces=driver.find_element_by_xpath('//span[@title = "{}"]'.format("online"))
            if online==0:
                statedate=datetime.datetime.now().strftime("online: %y-%m-%d, %H:%M")
                online=1
                print("online")
                return(statedate)
        except:
            if online==1:
                statedate=datetime.datetime.now().strftime("ofline: %y-%m-%d, %H:%M")
                online=0
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


    return render(request, 'index.html', {'stalkingacces': stalkingacces}, c)
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
    #     def qrCodeRead():
    #         time.sleep(3)
    #         qrCode = driver.find_element_by_class_name('_2EZ_m')
    #         qrCodeHtml=qrCode.get_attribute('innerHTML')
    #         return qrCodeHtml
    #
    #     qrCodeRead()
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
