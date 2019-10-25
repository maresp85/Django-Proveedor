from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#se importan todas las vistas de la aplicación categorias
from .views import ProductoList, ProductoCreate, ProductoDelete, ProductosAPI

app_name = 'producto'
urlpatterns = [
    path('listar/', ProductoList.as_view(), name='listar'),
    path('crear/', ProductoCreate.as_view(), name='crear'),
    path('eliminar/<int:pk>/', ProductoDelete.as_view(), name='eliminar'),
    #api
    path('api/', ProductosAPI.as_view(), name='api'),
    path('api/<int:pk>', ProductosAPI.as_view(), name='api'),
]
