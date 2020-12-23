from django.contrib import admin
from shop.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug', 'price')
    list_filter = ('category', 'available')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
