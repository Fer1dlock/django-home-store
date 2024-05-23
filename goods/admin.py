from django.contrib import admin

from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price', 'quantity', 'category')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
