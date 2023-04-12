from django import forms


class DiscountVoucherForm(forms.Form):
    code = forms.CharField()
