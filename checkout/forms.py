from django import forms
from .models import Order


class CreatingOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name','surname', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
