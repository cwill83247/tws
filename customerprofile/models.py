from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)              #USED FOR FIRST NAME CAN I CONCATENATE ?
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20, null=True, blank=False)                 #set Null=True on alot of fields whilst one migration -----
    street_address1 = models.CharField(max_length=80, null=True , blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=False)
    #county = models.CharField(max_length=80, null=True, blank=True)                          
    postcode = models.CharField(max_length=20, null=True, blank=True)    
    country = CountryField(blank_label='Country *', null=True , blank=False)            #  set Null = True to workaround re visit country dropdown issue 

    def __str__(self):
        return self.name