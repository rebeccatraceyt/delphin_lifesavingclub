from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('review/', views.order_review, name='order_review'),
    path('details/', views.order_details, name='order_details'),
]
