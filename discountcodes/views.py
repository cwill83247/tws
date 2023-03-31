from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import DiscountVoucherForm
from shoppingbag import views
from shoppingbag import contexts
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

            bag = request.session.get('bag')                       
            current_bag = shoppingbag_contents(request)
            get_order_total = current_bag['total']
            print('valid code')  
            savings = (voucher.amountpercentage / Decimal(100)) * get_order_total
            print("savings",savings)                        
            get_order_total_after_discount = get_order_total - savings
            get_order_total_after_discount = float(get_order_total_after_discount)   #31/3 had to convert to float otherwise gettign JSon seralize errors
            print("total after discount", get_order_total_after_discount) 
            request.session['christest'] = get_order_total_after_discount             #31/3 TEST
            christestgrabbedfromsession = request.session.get('christest')              # 31/3 TEST
            print("value form session", christestgrabbedfromsession)                # 31/3 TEST
                                  
            print(code)
            print(voucher.expiry_date)
            print(voucher.amountpercentage)
           
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
            print('invalid code')                     
      
    context = {
        'voucher.id': voucher.id,
        'code': code,
        'amountpercentage': voucher.amountpercentage,
        'savings': savings,
        'get_order_total_after_discount': get_order_total_after_discount,
        
    }
    return render(request, 'shoppingbag/bagcontents.html', context)             

