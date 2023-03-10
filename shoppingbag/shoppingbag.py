from decimal import Decimal
from django.conf import settings
from decimal import Decimal
from shop.models import Product
from django.shortcuts import get_object_or_404


class Shopping_Bag:
    def __init__(self, request):
        """
        Initialize the shopping bag.
        """
        self.session = request.session
        twsshoppingbag = self.session.get(settings.SHOPPINGBAG_SESSION_ID)
        if not twsshoppingbag:
            # if no shopping bag create an empty one 
            twsshoppingbag = self.session[settings.SHOPPINGBAG_SESSION_ID] = {}
        self.bag = twsshoppingbag

    # iterate over items in bag and get them form the DB
    def __iter__(self):
        
        product_ids = self.bag.keys()
        products = Product.objects.filter(id__in=product_ids)
        bag = self.bag.copy()
        for product in products:
            bag[str(product.id)]['product'] = product
        for item in bag.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    #adding product to the shopping bag checking if an item with same
    #product id is present 
    def add(self, product, quantity=1, override_quantity=False):

        product_id = str(product_id)
        if product_id not in self.cart:
            self.bag[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        #if true prpduct/item is int he bag so increase the quantity                            
        if override_quantity:
            self.bag[product_id]['quantity'] = quantity
        else:
            self.bag[product_id]['quantity'] += quantity
            self.save()
    
    #remove product/item form the shopping bag
    def remove(self, product):
       
        product_id = str(product.id)
        if product_id in self.bag:
            del self.cart[product_id]
            self.save()

     # removes session for shopping bag do i need this ?????
    def clear(self):
        del self.session[settings.SHOPPINGBAG_SESSION_ID]
        self.save()

    #update total 
    def get_order_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.bag.values())


    # setting boolean to make sure we save session data
    #changing session.modified to True DJANGO will know to save  
    def save(self):        
        self.session.modified = True        

