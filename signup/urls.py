from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='sigin'),
    path('signup', views.signup, name='signup'),
]