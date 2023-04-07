from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import *
from django.http import JsonResponse
import json

from shop.models import Product 
from checkout.models import Order, OrderItem
from customerprofile.models import Customer
from django.contrib.auth.models import User      
from django.contrib import messages
from discountcodes.forms import DiscountVoucherForm


# view contents of shopping bag
def view_shoppingbag(request):
    apply_coupon_form = DiscountVoucherForm()              #pulls in forms.py and discount field 
    return render(request, 'shoppingbag/bagcontents.html', {'apply_coupon_form': apply_coupon_form})


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
    messages.success(request, 'sucessfully added to your shopping bag')                                
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)   
    quantity = int(request.POST.get('quantity')) 
    bag = request.session.get('bag', {})                                 # added 13/3 @ 09:08  
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))


#removing items from the bag 
def remove_from_bag(request, item_id):
    bag = request.session["bag"]
    try:
        product = get_object_or_404(Product, pk=item_id)      #here we addign the product variable so can be used... in our messages 
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        
        return HttpResponse(status=200)  

    except Exception as e: 
        print(e)
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)     


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