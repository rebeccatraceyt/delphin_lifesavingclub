from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('review/', views.order_review, name='order_review'),
    path('details/', views.order_details, name='order_details'),
    path('complete/<order_number>', views.order_complete,
         name='order_complete'),
    path('wh/', webhook, name='webhook'),
]
