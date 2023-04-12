"""twsshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
       path('', views.product_list, name="product_list"),
       path('<int:id>/', views.product_detail, name="product_detail"),
       path('add/', views.add_product, name="add_product"),
       path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
       path('delete/<int:product_id>/', views.delete_product,
            name="delete_product"),
       path('product_admin/', views.product_admin, name="product_admin"),
]
