from django import forms
from .models import Contact
from django.forms import Textarea


class ContactForm(forms.ModelForm):
    """
    Form for user to contact us
    """
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'message'
        ]
        widgets = {
            'message': Textarea(
                attrs={
                    "placeholder": "How can we help you ?"
                }
            )
        }