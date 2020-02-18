from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
#   path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('article/', include('albums.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include(("core.urls", "products"), namespace = 'products' )),
    path('country/', include('country.urls')),
    path('city/', include('grouby_example.urls')),
    path('bootstrap_form/', include(('bootstrap_form.urls', 'bootstrap_form'), namespace="boot_form")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
                                    settings.STATIC_URL, 
                                    document_root = settings.STATIC_ROOT
                                )
    urlpatterns = urlpatterns + static(
                                    settings.MEDIA_URL, 
                                    document_root=settings.MEDIA_ROOT
                                )