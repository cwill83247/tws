# home app urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('ourstory/', views.ourstory, name='ourstory'),  
    path('sponsoredriders/', views.sponsoredriders, name='sponsoredriders'),  
]

