from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import view_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', view_home, name='home'),
    path('shop/', include('shop.urls')),
]

# Check debug status
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
