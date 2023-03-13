from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['order_number','id', 'first_name', 'surname', 'email',
                    'street_address1','street_address2', 'postcode', 'town_or_city', 'paid',
                    'created', 'updated']

    readonly_fields = ('order_number',)                
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

