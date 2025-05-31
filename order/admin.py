from traceback import format_tb
from django.contrib import admin
from django.utils.html import format_html
from .models import Sevimlilar, AddToShopCart, Payment



@admin.register(Sevimlilar)
class SevimlilarAdmin(admin.ModelAdmin):
     list_display = ['user', 'product']
     list_display_links = ['user', 'product']
     search_fields = ['user', 'product']
     lis_per_page = 10



@admin.register(AddToShopCart)
class AddToShopCartAdmin(admin.ModelAdmin):
     list_display = ['user', 'product', 'quantity', 'created_at', 'status', 'is_active']
     list_display_links = ['user', 'product']
     search_fields = ['user', 'product', 'quantity']
     list_editable = ['status', 'is_active']
     lis_per_page = 10




@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
     list_display = [
          "id", "ordered_by", "ordered", "country", "address", "phone", "created_at", "is_active"
     ]
     list_display_links = ["id", "country", "address"]
     list_editable = ["is_active"]
     search_fields = ["country", "address", "phone", "payment_method"]
     list_filter = ["payment_method"]
     list_per_page = 10

     def ordered_by(self, obj):
          users = {order.user.username for order in obj.order.all()}
          return ", ".join(users)
     ordered_by.short_description = "Buyurtmachi"

     def ordered(self, obj):
          products = [order.product.model for order in obj.order.all()]
          return ", ".join(products)
     ordered.short_description = "Buyurtmalari"




