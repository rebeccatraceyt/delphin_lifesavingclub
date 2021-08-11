from django.contrib import admin
from .models import SwimCategory, SwimProgramme, FAQ


# ------ Swim Categories ------


class SwimCategoryAdmin(admin.ModelAdmin):
    """
    Create admin views for Categories
    """
    list_display = (
        'name',
        'friendly_name',
    )


# ------ Swim Programme ------


class SwimProgrammeAdmin(admin.ModelAdmin):
    """
    Create admin views for Swim Programmes
    """
    list_display = (
        'name',
        'description',
        'age',
        'swim_category',
    )


# ------ FAQs ------


class FAQAdmin(admin.ModelAdmin):
    """
    Create admin views for FAQs
    """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(SwimCategory, SwimCategoryAdmin)
admin.site.register(SwimProgramme, SwimProgrammeAdmin)
admin.site.register(FAQ, FAQAdmin)
