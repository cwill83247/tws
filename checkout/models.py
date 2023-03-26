import uuid 
from decimal import Decimal
from django.db import models
from django.conf import settings
from shop.models import Product, Category
from django.db.models import Sum
from django_countries.fields import CountryField


# Order 
class Order(models.Model):
    order_number = models.CharField(max_length=200, null=True, editable=False)             ## 18/3/23 Need ot Add Discount code and Store the Ammount of Discount 
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
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

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

    def update_total(self):                                                             ## 18/3/23 ADD Logic for Discount or create another Function that runs Prior !!
        """
        Update grand total within this class above each time a line item is added,
        including delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY) 
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()       

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
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the DEFAULT save method to set the order number
        if it doesnt have one.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product Code {self.product.product_code} on order {self.order.order_number}'       

