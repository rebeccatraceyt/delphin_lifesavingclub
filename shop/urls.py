from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('add/', views.add_product, name='add_product'),
    path('search', views.search, name='search'),
    path('product/<product_id>', views.product_detail, name='product_detail'),
    path('courses', views.courses, name='courses'),
    path('apparel', views.apparel, name='apparel'),
]
