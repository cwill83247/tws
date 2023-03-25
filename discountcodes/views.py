from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import DiscountVoucherForm
from shoppingbag import views
from shoppingbag.contexts import shoppingbag_contents
from decimal import Decimal
# Create your views here.

@require_POST
def apply_voucher(request):
    now = timezone.now()
    form = DiscountVoucherForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
                                          expiry_date__gte=now, active=True)
            request.session['voucher_id'] = voucher.id

           
            # bag = request.session.get('bag')                        ## dont think its needed added 19.36
            current_bag = shoppingbag_contents(request)
            print("current bag", current_bag)
            get_order_total = current_bag['total']
            print("get order total",get_order_total)
            print('valid code')  
             ###   added @ 17:51
            savings = (voucher.amountpercentage / Decimal(100)) * get_order_total
            print("savings",savings)                        
            get_order_total_after_discount = get_order_total - savings
            print("total after discount", get_order_total_after_discount)    

           
            print(code)
            print(voucher.expiry_date)
            print(voucher.amountpercentage)
            # TROUBLESHOOTING
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
            print('invalid code')                        # TROUBLESHOOTING
    
    # return redirect('/shoppingbag')                   ## Unsure on Redirect I need to return some Context back to Browser to USE ???
    context = {
        'voucher.id': voucher.id,
        'code': code,
        'amountpercentage': voucher.amountpercentage,
        'savings': savings,
        'get_order_total_after_discount': get_order_total_after_discount,
    }
    return render(request, 'shoppingbag/bagcontents.html', context) 

