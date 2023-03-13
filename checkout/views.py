from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Order, OrderItem
from .forms import CreatingOrderForm
from shoppingbag.contexts import shoppingbag_contents
# Create your views here.


