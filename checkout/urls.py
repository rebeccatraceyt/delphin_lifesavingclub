from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('info/', views.order_info, name='order_info'),
]
