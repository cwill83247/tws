import uuid 
from django.db import models
from django.conf import settings
from shop.models import Product, Category
from django.db.models import Sum
from django_countries.fields import CountryField


# Order 
class Order(models.Model):
    order_number = models.CharField(max_length=200, null=True, editable=False)              #failing for some reason 
    first_name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20, null=True, blank=False)                 #set Null=True on alot of fields whilst one migration -----
    street_address1 = models.CharField(max_length=80, null=True , blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)                          
    postcode = models.CharField(max_length=20, null=True, blank=True)    
    country = CountryField(blank_label='Country *', null=True , blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
    
    def _generate_order_number(self):                                  
        """
        Generate a random number for order number using UUID
        """
        return uuid.uuid4().hex.upper()     

    def save(self, *args, **kwargs):
        """
        Override the DEFAULT save method to set the order number
        if it doesnt have one.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()  #calls generate order function 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    

    # need to add in link for stripe so can store payment ID use of webhooks to confirm payment          

#each item added to the Order 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='lineitems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Product Code {self.product.product_code} on order {self.order.order_number}'       

