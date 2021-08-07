from django.contrib import admin
from .models import (
    Category,
    Time,
    Size,
    Product,
    CourseTime,
    ApparelSize,
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


# ------ Courses Tables and Filters ------


class CourseTimeInline(admin.TabularInline):
    """
    Defines inline class for Course Time
    """
    model = CourseTime
    extra = 1


class TimeAdmin(admin.ModelAdmin):
    """
    Create admin views for Course Times
    """
    inlines = (CourseTimeInline,)
    list_display = (
        'time',
        'time_name',
    )


# ------ Apparel Tables and Filters ------


class ApparelSizeInline(admin.TabularInline):
    """
    Defines inline class for Apparel Size
    """
    model = ApparelSize
    extra = 1


class SizeAdmin(admin.ModelAdmin):
    """
    Create admin views for Apparel Sizes
    """
    inlines = (ApparelSizeInline,)
    list_display = (
        'size',
        'size_name',
    )


# ------ All Products ------


class ProductAdmin(admin.ModelAdmin):
    """
    Create admin views for all Products
    """
    inlines = (CourseTimeInline,
               ApparelSizeInline,)
    list_display = (
        'name',
        'description',
        'price',
        'category',
        'is_course',
        'is_apparel',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
