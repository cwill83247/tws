from django.contrib import admin
from .models import Voucher
# Register your models here.


@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ['code', 'description',
                    'amountpercentage', 'expiry_date','active'] 
    search_fields = ['code']