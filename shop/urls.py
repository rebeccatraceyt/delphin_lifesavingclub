from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('all_courses', views.all_courses, name='all_courses'),
    path('all_apparel', views.all_apparel, name='all_apparel'),
]
