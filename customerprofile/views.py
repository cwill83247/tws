from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerProfileForm
from checkout.models import Order
from django.http import Http404


@login_required
def profile(request):
    """ Display and Edit Customer profile. """
    try:
        profile = get_object_or_404(Customer, user=request.user)
    except Http404:
        return redirect('new_profile/')

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = CustomerProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'customerprofile/customerprofile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def new_profile(request):
    """ create new Customer profile. """
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            """ set the user to account logged in"""
            profile.user = request.user
            profile.save()

            messages.success(request, 'Profile created successfully')
        else:
            messages.error(request, 'Creation Failed. Please ensure the form is valid.')
    else:
        form = CustomerProfileForm()

    template = 'customerprofile/new_customerprofile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
