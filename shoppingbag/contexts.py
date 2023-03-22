
#making my shopping bag contents across the whole site
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from discountcodes.forms import DiscountVoucherForm


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    # discount code /voucher
    voucher_id = request.session.get('voucher_id')     ###22/3/23 Voucher
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shoppingbag_items.append({       #adding items into our shopping bag dictonairy 
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

     # discount code/voucher check if in session                                                 #22/3 - VOUCHER
    
    def voucher(request):
        if voucher_id:
            try:
                return Voucher.objects.get(id=voucher_id)
            except Voucher.DoesNotExist:
                pass
        return None

    def apply_voucher(request):
        if voucher:
            return (voucher.amountpercentage / Decimal(100))  \
                    * get_order_total()
        return Decimal(0)

    def get_order_total_after_discount(self):
        return get_order_total() - apply_discount()

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total    

    context = {
        'shoppingbag_items': shoppingbag_items, 
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'get_order_total_after_discount': get_order_total_after_discount,                         ##Will this work 22/2 @ 17:36
    }

    return context