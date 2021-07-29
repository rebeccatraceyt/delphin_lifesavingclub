from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pages.views import view_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', view_home, name='home'),
    path('products/', include('products.urls')),
]

# Check debug status
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
