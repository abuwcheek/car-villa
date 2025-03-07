from django.contrib import admin
from .models import Sevimlilar, AddToShopCart, Payment



@admin.register(Sevimlilar)
class SevimlilarAdmin(admin.ModelAdmin):
     list_display = ['user', 'product']
     list_display_links = ['user', 'product']
     search_fields = ['user', 'product']
     lis_per_page = 10



@admin.register(AddToShopCart)
class AddToShopCartAdmin(admin.ModelAdmin):
     list_display = ['user', 'product', 'quantity']
     list_display_links = ['user', 'product']
     search_fields = ['user', 'product', 'quantity']
     lis_per_page = 10



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
     list_display = ['country', 'address', 'phone', 'total']
     list_display_links = ['country', 'phone']