
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.profile, name='profile'), 
    path('order_history/<order_number>', views.order_history, name='order_history'),   
]