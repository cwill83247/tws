
#making my shopping bag contents across the whole site
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    context = {
        'shoppingbag_items': shoppingbag_items, 
        'total': total,
        'product_count': product_count,
    }

    return context