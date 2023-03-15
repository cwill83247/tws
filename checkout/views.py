from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Order, OrderItem
from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
from django.contrib import messages
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you shopping bag is empty")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MU7oOIe6TtZVkRYjIeZw2c8jb6wK1b4BELD6fXtC8tnhZefKnyBpM5i5oKTXgZQvNWbgPty0YT4KpxoL1WYEEA300Q3CHeWcV',
        'client_secret': 'cw12345678test',
    }

    return render(request, template, context)