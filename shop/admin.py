from django.contrib import admin
from .models import (
    ProductType,
    Time,
    AgeRange,
    Course,
    CourseTime,
    Size,
    Category,
    Apparel,
    ApparelSize
)


# ------ Product Types ------


class ProductTypeAdmin(admin.ModelAdmin):
    """
    Create admin views for Product Types
    """
    list_display = (
        'name',
        'friendly_name',
    )


# ------ Courses ------


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


class AgeRangeAdmin(admin.ModelAdmin):
    """
    Create admin views for Ages
    """
    list_display = (
        'name',
        'friendly_name',
    )


class CourseAdmin(admin.ModelAdmin):
    """
    Create admin views for Course
    """
    inlines = (CourseTimeInline,)
    list_display = (
        'product_type',
        'name',
        'description',
        'price',
        'lvl_age',
        'age_range',
        'image',
    )


# ------ Apparel ------


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


class CategoryAdmin(admin.ModelAdmin):
    """
    Create admin views for Categories
    """
    list_display = (
        'name',
        'friendly_name',
    )


class ApparelAdmin(admin.ModelAdmin):
    """
    Create admin views for Apparel
    """
    inlines = (ApparelSizeInline,)
    list_display = (
        'product_type',
        'name',
        'description',
        'price',
        'category',
        'image',
    )


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(AgeRange, AgeRangeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Apparel, ApparelAdmin)
