from django.contrib import admin

from .models import Category, Brands, CarVilla



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     search_fields = ('created_at')
     