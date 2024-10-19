from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Brands, CarVilla, CarImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     search_fields = ['id', 'created_at']
     list_editable = ['is_active']
     prepopulated_fields = {'slug': ['name']}



@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
     list_display = ('name', 'icon', 'created_at', 'is_active')
     list_display_links = ('name', 'icon',)
     list_editable = ['is_active']
     


class CarImageInline(admin.StackedInline):
    readonly_fields = ('get_image', 'updated_at')
    model = CarImage
    extra = 1



@admin.register(CarVilla)
class CarVillaAdmin(admin.ModelAdmin):
     inlines = [CarImageInline]
     list_display = ('model', 'category', 'brand', 'year', 'price', 'views', 'created_at', 'is_active')
     list_display_links = ('model', 'category', 'brand')
     search_fields = ['id', 'model', 'price', 'views', 'created_at',]
     list_editable = ['is_active']
     list_per_page = 20
     readonly_fields = ['views']
     list_filter = ['price', 'year', 'views']