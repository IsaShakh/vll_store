from django.contrib import admin
from .models import *


class ColorTabularInline(admin.TabularInline):
    model = Color


class ImageTabularInline(admin.TabularInline):
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['name', 'is_active']
    search_fields = ['name', 'is_active']


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['name', 'is_active']
    search_fields = ['name', 'is_active']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'category']
    list_filter = ['is_active', 'category']
    search_fields = ['name', 'is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorTabularInline, ImageTabularInline]
    list_display = ['name', 'price', 'posted_at', 'updated_at', 'to_remove']
    list_filter = ['name', 'category', 'subcategory', 'style', 'to_remove']
    search_fields = ['name', 'category', 'subcategory', 'style']
    list_editable = ['to_remove', ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

