from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'postcode',
        'country',
    )

    ordering = ('user',)


admin.site.register(Customer, CustomerAdmin)
