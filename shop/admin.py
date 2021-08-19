from django.contrib import admin
from .models import (
    Category,
    ProductOption,
    Product,
    ProductSelect,
)


# ------ Product Categories ------


class CategoryAdmin(admin.ModelAdmin):
    """
    Create admin views for Categories
    """
    list_display = (
        'name',
        'friendly_name',
    )


# ------ Product Table (product + variation) ------


class ProductSelectInline(admin.TabularInline):
    """
    Defines inline class for Product variations
    """
    model = ProductSelect
    extra = 1


# ------ Product Filters ------


class ProductOptionAdmin(admin.ModelAdmin):
    """
    Create admin views for Product Variations
    """
    inlines = (ProductSelectInline,)
    list_display = (
        'product_option',
        'option_name',
    )


# ------ All Products ------


class ProductAdmin(admin.ModelAdmin):
    """
    Create admin views for all Products
    """
    inlines = (ProductSelectInline,)
    list_display = (
        'name',
        'description',
        'price',
        'category',
        'is_course',
        'is_apparel',
        'image_tag',
    )


# Register Product, Product Options and Category models
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(Product, ProductAdmin)
