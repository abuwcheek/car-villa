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
     list_display = ["id", "ordered_by", "country", "address", "phone", "payment_method", "plastic_card", "card_name", "expiration_date", "payment_check_link", "created_at", "is_active"]
     list_display_links = ["id", "country", "address"]
     list_editable = ["payment_method", "plastic_card", "card_name", "expiration_date", "is_active"]
     search_fields = ["country", "address", "phone", "payment_method"]
     list_filter = ["payment_method"]
     list_per_page = 10

     def ordered_by(self, obj):
          """Buyurtmani bergan foydalanuvchini ko‘rsatish"""
          return obj.order.user if obj.order.user else "Noma'lum"

     ordered_by.short_description = "Buyurtmachi"

     def payment_check_link(self, obj):
          """Admin panelda yuklangan fayl yoki rasmni ko‘rsatish"""
          if obj.payment_check and obj.payment_check.url:
               content_type = getattr(obj.payment_check.file, "content_type", "")
               if content_type.startswith("image"):
                    return format_html('<img src="{}" width="100" height="100" style="border-radius:5px;" />', obj.payment_check.url)
               return format_html('<a href="{}" target="_blank" download>Chekni yuklab olish</a>', obj.payment_check.url)
          return "Chek yuklanmagan"

     payment_check_link.short_description = "To‘lov Cheki"