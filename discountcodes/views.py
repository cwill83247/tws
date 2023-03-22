from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import DiscountVoucherForm
from shoppingbag import views

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
            print('valid code')   
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
    }
    return render(request,
                  'shoppingbag/bagcontents.html',
                  {'voucher.id': voucher.id,
                   'code': code,
                   'voucher.amountpercentage': voucher.amountpercentage}) 
