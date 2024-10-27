from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Brands, CarVilla, CarImage, Testimonals, About



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     search_fields = ['id', 'created_at']
     list_editable = ['is_active']
     prepopulated_fields = {'slug': ['name']}



@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
     list_display = ('name','display_icon', 'created_at', 'is_active')
     list_display_links = ('name', 'display_icon',)
     list_editable = ['is_active']
     readonly_fields = ('id', 'display_icon')

     def display_icon(self, obj):
          # return mark_safe('<img src="%s" width="100" height="100" />' % obj.icon.url)
          return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.icon.url))

     display_icon.allow_tags = True
     display_icon.short_description = 'Icon'
     


class CarImageInline(admin.StackedInline):
    readonly_fields = ('get_image', 'updated_at')
    model = CarImage
    extra = 1



@admin.register(CarVilla)
class CarVillaAdmin(admin.ModelAdmin):
     inlines = [CarImageInline]
     list_display = ('model', 'category', 'brand', 'year', 'price', 'views', 'created_at', 'is_active', 'is_featured', 'is_published' )
     list_display_links = ('model', 'category', 'brand')
     search_fields = ['id', 'model', 'price', 'views', 'created_at',]
     list_editable = ['is_active', 'is_featured', 'is_published']
     list_per_page = 20
     readonly_fields = ['views']
     list_filter = ['price', 'year', 'views']



@admin.register(Testimonals)
class TestimonalsAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'country', 'is_active', 'created_at')
     list_display_links = ('full_name', 'country')
     list_editable = ['is_active']



admin.site.register(About)