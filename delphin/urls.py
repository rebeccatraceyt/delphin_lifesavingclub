from django.contrib import admin
from django.urls import path, include
from pages.views import view_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', view_home, name='home'),
]
