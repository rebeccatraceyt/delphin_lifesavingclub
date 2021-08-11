from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.view_contact, name='view_contact'),
    path('swim_programme', views.view_programme, name='view_programme'),
]
