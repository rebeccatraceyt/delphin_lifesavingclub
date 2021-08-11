from django.urls import path
from . import views

urlpatterns = [
    path('swim_programme', views.view_programme, name='view_programme'),
]
