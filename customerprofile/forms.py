from django import forms
from .models import Customer


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'surname', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',)
    
    # advanced form customisation from Code Institute 
    def __init__(self, *args, **kwargs):
        """
        Override the Default init method so we can
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on email field
        """
        super().__init__(*args, **kwargs)
        """ 
        changing so names appear more 
        user friendly on the form to its Db field name 
        """
        placeholders = {
            'first_name': 'First Name',
            'surname': 'Surname',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street and house number',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }  
        """
        adding * on required fields
        setting focus on email field 
        1st on the form
        """
        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            """
            below set to false so we
            use the placeholders created above
            """
            self.fields[field].label = False