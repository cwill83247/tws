from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)              
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20, null=True, blank=False)                
    street_address1 = models.CharField(max_length=80, null=True, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=False)                       
    postcode = models.CharField(max_length=20, null=True, blank=True)    
    country = CountryField(blank_label='Country *', null=True, blank=False)           


    # returns username 

    def __str__(self):
        return self.user.username

