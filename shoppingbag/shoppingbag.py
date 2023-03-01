from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.shortcuts import get_object_or_404


Class Shopping_Bag:
    def __init__(self, request):
        """
        Initialize the shopping bag.
        """
        self.session = request.session
        twsshoppingbag = self.session.get(settings.SHOPPINGBAG_SESSION_ID)
        if not twsshoppingbag:
            # if no shopping bag create an empty one 
            twsshoppingbag = self.session[settings.SHOPPINGBAG_SESSION_ID] = {}
        self.cart = twsshoppingbag