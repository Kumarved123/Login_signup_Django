from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from signup.forms import RegistrationForm
from django.contrib import messages
from django.conf import settings
from django.contrib.sessions.models import Session

import json
import urllib

# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
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
            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('index')
            
        else:
            messages.error(request,'Invalid Credentials, Try Again !!!!')
            return redirect('index')

    else:
        form = RegistrationForm()

        args = {'form': form }
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

