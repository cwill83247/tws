from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from django.conf import settings
from .models import Order, OrderItem
from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
from discountcodes import views
from django.contrib import messages
from shop.models import Product
import stripe
import json
from django.views.decorators.http import require_POST
from customerprofile.models import Customer
from customerprofile.forms import CustomerProfileForm


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                print("BAG")
                print(item_id)
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderItem(
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
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
            # end of for loop
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            print(order_form.errors.as_data())
    else:
        bag = request.session.get('bag', {})

        if not bag:
            messages.error(request, "Looks like you shopping bag is empty")
            return redirect(reverse('shop'))

        current_bag = shoppingbag_contents(request)

        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        """
        connecting to Stripe to create Payment Intent
        using Stripes API and secret key
        from above > via environment variables
        """

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency="gbp",
        )
        # if user is logged in pre-populate form, from customerprofile

        if request.user.is_authenticated:
            try:
                profile = Customer.objects.get(user=request.user)
                print(profile.name)
                order_form = OrderForm(initial={
                    'email': profile.email,
                    'phone_number': profile.phone_number,
                    'first_name': profile.name,
                    'surname': profile.surname,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'town_or_city': profile.town_or_city,
                    'postcode': profile.postcode,
                    'country': profile.country,
                })
            except Customer.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
    print(intent)

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

    # checking if user is logged in and saving order to ther profile
    # try added becuase osme users dont have a profile initially

    if request.user.is_authenticated:
        try:
            profile = Customer.objects.get(user=request.user)
            order.user_profile = profile
            order.save()
            messages.success(request, f'Order Completed!,your order number is')
        except:
            messages.success(request, f'Consider creating a profile to save your delivery information, and enable faster checkouts')

    # if success redirect customer and clear the shopping bag so empty
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
