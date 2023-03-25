from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]