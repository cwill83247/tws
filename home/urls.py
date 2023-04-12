# home app urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ourstory/', views.ourstory, name='ourstory'),
    path('sponsoredriders/', views.sponsoredriders, name='sponsoredriders'),
]
