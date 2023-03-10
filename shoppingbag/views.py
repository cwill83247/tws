from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import *
from django.http import JsonResponse
import json

#import 
from shop.models import Product 
from checkout.models import Order, OrderItem
from customerprofile.models import Customer
from django.contrib.auth.models import User                        ####??


# view contents of shopping bag
def view_shoppingbag(request):
    
    return render(request, 'shoppingbag/bagcontents.html')


# add product , quantity of product to shopping bag using form method
def add_to_bag(request, item_id):
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

# Possibly Remove as using JS to Listen and then call ???? Function for when item is added to shopping bag
def updateItem(request):
    data = json.loads(request.body)                      ###10/3 
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Prpdcut Id:', productId)

    customer = request.user.customer    
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, paid=False)  #come from checkout/models.py 

    bag = request.session.get('bag', {})             # this is key as creates in  the http session and stores it until user closes browser   

    if productId in list(bag.keys()):
        bag[productId] += quantity
    else:
        bag[productId]  = quantity
    
    request.session['bag'] = bag
    return JsonResponse('Item add to bag', safe=False)