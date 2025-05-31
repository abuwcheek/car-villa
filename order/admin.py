from django.contrib import admin
from .models import Sevimlilar, AddToShopCart, Payment


class AddToShopCartInline(admin.TabularInline):
     model = Payment.order.through
     extra = 0
     readonly_fields = ('addtoshopcart',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
     list_display = ('id', 'payment_method', 'country', 'phone', 'created_at')
     list_filter = ('payment_method', 'created_at')
     search_fields = ('country', 'phone')
     inlines = [AddToShopCartInline]
     readonly_fields = ('created_at', 'updated_at')


@admin.register(AddToShopCart)
class AddToShopCartAdmin(admin.ModelAdmin):
     list_display = ('user', 'product', 'quantity', 'status', 'total_price')
     list_filter = ('status', 'created_at')
     search_fields = ('user__username', 'product__model')
     readonly_fields = ('total_price', 'created_at', 'updated_at')


@admin.register(Sevimlilar)
class SevimlilarAdmin(admin.ModelAdmin):
     list_display = ('user', 'product')
     search_fields = ('user__username', 'product__model')