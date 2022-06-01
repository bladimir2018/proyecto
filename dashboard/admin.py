from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header='INVENTARIO'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity', 'category')

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.register(Group)