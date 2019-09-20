from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from shops.models import Shop

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
