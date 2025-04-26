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
     list_display = ['id', 'country', 'address', 'phone', 'payment_method', 'plastic_card', 'card_name', 'expiration_date', 'total', 'ordered_products', 'created_at', 'payment_check_link', 'is_active']
     list_display_links = ['id', 'country', 'address']
     list_editable = ['payment_method', 'is_active']
     search_fields = ['country', 'address', 'phone', 'payment_method', 'plastic_card', 'card_name']
     list_filter = ['country', 'address', 'phone', 'payment_method', 'plastic_card', 'card_name']
     list_per_page = 10

     
     def ordered_products(self, obj):
          if obj.order.exists():  # 🛠 Mahsulotlar borligini tekshirish
               return ", ".join([f"{o.product.model} (x{o.quantity})" for o in obj.order.all()])
          return "Mahsulotlar yo'q"  # 🔥 Agar mahsulot yo‘q bo‘lsa
     
     ordered_products.short_description = "Tanlangan mahsulotlar"


     from django.utils.html import format_html

     def payment_check_link(self, obj):
          if obj.payment_check:
               return format_html(
                    '<a href="{}" target="_blank" download>Chekni yuklab olish</a>',
                    obj.payment_check.url
               )
          return "Chek yuklanmagan"
     payment_check_link.allow_tags = True  # ✅ HTML havola ishlashi uchun
     payment_check_link.short_description = "To‘lov Cheki"
