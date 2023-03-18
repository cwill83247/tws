from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings 
from .models import Order, OrderItem
from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
from django.contrib import messages
import stripe


# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like you shopping bag is empty")
        return redirect(reverse('shop'))

    current_bag = shoppingbag_contents(request)
    print(current_bag)

    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    # connecting to Stripe to create Payment Intent
    # using Stripes API and secret key from above > via environment variables 

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency="gbp",
        )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MU7oOIe6TtZVkRYjIeZw2c8jb6wK1b4BELD6fXtC8tnhZefKnyBpM5i5oKTXgZQvNWbgPty0YT4KpxoL1WYEEA300Q3CHeWcV',
        'client_secret': 'cw12345678test',
    }

    return render(request, template, context)