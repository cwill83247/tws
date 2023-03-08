from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your views here.


# Function for when item is added to shopping bag
def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Prpdcut Id:', productId)

    return JsonResponse('Item add to bag', safe=False)