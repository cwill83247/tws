from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)
    raw_id_fields = ['product']

 
                                    ### will need to add in Discount code Applied and Discount Amount
class OrderAdmin(admin.ModelAdmin):

    list_display = ['order_number', 'id', 'email',
                    'order_total', 'delivery_cost', 'grand_total',  'town_or_city', 'paid',
                    'created', 'updated']

    readonly_fields = ('order_number', 'delivery_cost', 'order_total', 'grand_total')                
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
