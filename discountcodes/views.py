from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import DiscountVoucherForm
from shoppingbag import views
from shoppingbag import contexts
from shoppingbag.contexts import shoppingbag_contents
from decimal import Decimal
from django.contrib import messages
# Create your views here.

@require_POST
def apply_voucher(request):
    now = timezone.now()
    form = DiscountVoucherForm(request.POST)

    voucher = None  # 11/4/23 Invalid voucher issue 
    
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
                                          expiry_date__gte=now, active=True)
            request.session['voucher_id'] = voucher.id

            bag = request.session.get('bag')                       
            current_bag = shoppingbag_contents(request)
            get_order_total = current_bag['total']            
            savings = (voucher.amountpercentage / Decimal(100)) * get_order_total                                  
            get_order_total_after_discount = get_order_total - savings
            get_order_total_after_discount = float(get_order_total_after_discount)   
            request.session['christest'] = get_order_total_after_discount                              ## RENAME      
            christestgrabbedfromsession = request.session.get('christest')                             ## RENAME        
                       
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
            print('invalid code')
            messages.error(request, 'Sorry, Invalid or Expired Code.')                     

    context = {}                                                                                            # 11/4 added
    if voucher is not None:                                                                                 # 11/4 added         
        context = {
            'voucher.id': voucher.id,
            'code': code,
            'amountpercentage': voucher.amountpercentage,
            'savings': savings,
            'get_order_total_after_discount': get_order_total_after_discount,
            
        }
    return render(request, 'shoppingbag/bagcontents.html', context)             

