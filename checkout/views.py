from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Order, OrderItem
from .forms import CreatingOrderForm
from shoppingbag.contexts import shoppingbag_contents
from django.contrib import messages
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you shopping bag is empty")
        return redirect(reverse('shop'))

    order_form = CreatingOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'Your Order': order_form,
    }

    return render(request, template,context)