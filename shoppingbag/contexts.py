
#making my shopping bag contents across the whole site
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from discountcodes.forms import DiscountVoucherForm
from discountcodes import views


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    # discount code /voucher
    voucher_id = request.session.get('voucher_id')   

    discountedtotalcontext = request.session.get('discountedtotal_session')            
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shoppingbag_items.append({       # adding items into our shopping bag dictonairy 
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 100
    
    #if christestgrabbedfromsessionaddincontext: 
    if discountedtotalcontext:                                                                        #2/4/23 IF logic if code has been used
        grand_total = discountedtotalcontext + float(delivery)                                                      #2/4/23 IF logic if code has been used
    else:                                                                                                                    #2/4/23 IF logic if code has been used
        grand_total = delivery + total                                                                               
      
    context = {
        'shoppingbag_items': shoppingbag_items, 
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,   
        'discountedtotalcontext': discountedtotalcontext,
        'voucher_id': voucher_id,
        
    }    
    return context