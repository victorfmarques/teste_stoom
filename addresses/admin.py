from django.contrib import admin

from addresses.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_filter =('country', 'state', 'city', 'neighbourhood')
    search_fields = ('id', 'country', 'state', 'city', 'neighbourhood', 'street_name', 'zip_code', )
    list_display = ('id', 'country', 'state', 'city', 'neighbourhood', 'street_name', )
