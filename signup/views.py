from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from signup.forms import RegistrationForm
from django.contrib import messages
from django.conf import settings
from . models import Details
from datetime import datetime, timedelta

import json
import urllib

# Create your views here.
def register(request):
    # getting the Ip address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # getting check whether this ip exist in the databse or not
    try:
        detail = Details.objects.get(pk=ip)
    except :
        detail = None
    # if ip address exist
    if detail:
        expire = datetime.now()
        curr = datetime.strptime(str(detail.time_out)[:19], "%Y-%m-%d %H:%M:%S")
        
        if curr<expire:
            cap = False
            detail.delete()
            newip = Details.objects.create(ip_address= ip, attemps= 0, time_out= datetime.today() + timedelta(minutes=2))
            newip.save()
        else:
            #check the number of attemps
            if detail.attemps > 2:
                cap = True
                #dispaly the captcha
            else:
                cap = False
                #not dispaly of captcha
    # if ip address donot exist
    else:
        # not display of captcha
        cap = False
        newip = Details.objects.create(ip_address= ip, attemps= 0, time_out= datetime.today() + timedelta(minutes=2))
        newip.save()

    if request.method =='POST':
        if detail:
            detail.attemps = detail.attemps + 1
            detail.save()
        else:
            newip.attemps = newip.attemps + 1
            newip.save()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if cap:
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
            else:
                result = {'success':True}
            if result['success']:
                form.save()
                messages.success(request, 'New Account created with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('index')
            
        else:
            messages.error(request,'Invalid Credentials, Try Again !!!!')
            return redirect('index')
    else:
        if cap:
            p  = "block"
        else:
            p = "none"
        form = RegistrationForm()
        args = {'form': form, 'cap':p}
        return render(request, 'index.html', args)
def profile(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

