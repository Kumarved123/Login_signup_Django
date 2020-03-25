from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        d = dict(request.POST)
        if d['button'] == "login":
            username = d['username']
            password = d['password']
            return HttpResponse("You are logedin")
        if d['button'] == "signup":
            email = d['email']
            username = d['username']
            password = d['password']
            return HttpResponse("You are registered now")
    else:
        return render(request, 'index.html')
def signup(request):
    return HttpResponse("You are registered now")

def signin(request):
    return HttpResponse("You are logedin")