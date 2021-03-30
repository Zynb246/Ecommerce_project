from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
