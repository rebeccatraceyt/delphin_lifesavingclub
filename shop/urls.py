from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('all_courses', views.all_courses, name='all_courses'),
    path('course/<course_id>', views.course_detail, name='course_detail'),
    path('all_apparel', views.all_apparel, name='all_apparel'),
    path('apparel/<apparel_id>', views.apparel_detail, name='apparel_detail'),
    path('search', views.search, name='search'),
]
