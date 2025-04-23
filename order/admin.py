from traceback import format_tb
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
     list_display = ['user', 'product', 'quantity', 'created_at', 'status', 'is_active']
     list_display_links = ['user', 'product']
     search_fields = ['user', 'product', 'quantity']
     list_editable = ['status', 'is_active']
     lis_per_page = 10



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
     list_display = ['id', 'country', 'address', 'phone', 'payment_method', 'plastic_card', 'card_name', 'expiration_date', 'total', 'ordered_products', 'created_at']
     list_display_links = ['id', 'country', 'address']


     
     def ordered_products(self, obj):
          if obj.order.exists():  # 🛠 Mahsulotlar borligini tekshirish
               return ", ".join([f"{o.product.model} (x{o.quantity})" for o in obj.order.all()])
          return "Mahsulotlar yo'q"  # 🔥 Agar mahsulot yo‘q bo‘lsa
     
     ordered_products.short_description = "Tanlangan mahsulotlar"

     def payment_check_link(self, obj):
          if obj.payment_check:
               return f'<a href="{obj.payment_check.url}" target="_blank">Chekni ko‘rish</a>'
          return "Chek yuklanmagan"

     payment_check_link.allow_tags = True  # ✅ HTML havola ishlashi uchun
     payment_check_link.short_description = "To‘lov Cheki"
