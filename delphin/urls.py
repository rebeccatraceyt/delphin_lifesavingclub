from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import view_home


urlpatterns = [
    path('', view_home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('pages.urls')),
    path('shop/', include('shop.urls')),
    path('shopping_bag/', include('shopping_bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('users/', include('users.urls')),
]

# Error Handlers
handler400 = 'delphin.views.error_400_view'
handler403 = 'delphin.views.error_403_view'
handler404 = 'delphin.views.error_404_view'
handler500 = 'delphin.views.error_500_view'

# Check debug status
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
