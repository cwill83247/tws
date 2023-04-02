from django.contrib import admin#
from .models import Contact   

class ContactAdmin(admin.ModelAdmin):
    list_display = (
    'full_name',
    'email',
    'date_created', 
    )

    ordering = ('date_created',)


admin.site.register(Contact, ContactAdmin)
