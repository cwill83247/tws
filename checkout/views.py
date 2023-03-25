from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings 
from .models import Order, OrderItem
from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
from discountcodes import views
from django.contrib import messages
import stripe


# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],            
        }

        order_form = OrderForm(form_data)   ## create an instanc eof order form and put data into it   
        if order_form.is_valid():            
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    #if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                    
                except Product.DoesNotExist:
                    messages.error(request, (
                        "Sorry one of the items you added wasn't found ")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        
        if not bag:
            messages.error(request, "Looks like you shopping bag is empty")
            return redirect(reverse('shop'))

        current_bag = shoppingbag_contents(request)
        #print(current_bag)

        total = current_bag['grand_total']
        #stripe requires amount in an integer so converting to pence
        stripe_total = round(total * 100)

        # connecting to Stripe to create Payment Intent
        # using Stripes API and secret key from above > via environment variables 

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency="gbp",
            )

        #print(intent)

        order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        # secret below is returned from stripe payment intent
        # is used to create payment
        'client_secret': intent.client_secret,       
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order Completed!, your orde rnumber is {order_number}')

    # if success redirect customer and clear the shopping bag so empty
    if 'bag' in request.session:
        del request.session['bag']

    template =  'checkout/checkout_success.html'
    context = {
        'order':order ,
    }
    return render(request, template, context)   