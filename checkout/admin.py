from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    list_display = ['order_number', 'id', 'email',
                    'order_total', 'delivery_cost', 'grand_total',
                    'town_or_city', 'paid',
                    'order_dispatched', 'updated']

    readonly_fields = ('order_number', 'delivery_cost', 'order_total',
                       'grand_total')
    list_filter = ['paid', 'created', 'updated']


admin.site.register(Order, OrderAdmin)
