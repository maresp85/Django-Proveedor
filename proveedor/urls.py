from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoria/', include(('categoria.urls', 'categoria'), namespace='categoria')),
    path('producto/', include(('producto.urls', 'producto'), namespace='producto')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
