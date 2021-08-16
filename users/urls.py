from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('past_orders/', views.past_orders, name='past_orders'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
