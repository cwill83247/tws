from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

#import 
from shop.models import Product 
from customerprofile.models import Customer
from django.contrib.auth.models import User                        ####??

# Create your views here.


# Function for when item is added to shopping bag
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Prpdcut Id:', productId)

    customer = request.user.customer    
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    return JsonResponse('Item add to bag', safe=False)