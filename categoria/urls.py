from django.urls import path

#se importan todas las vistas de la aplicación categorias
from .views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete

app_name = 'categoria'
urlpatterns = [
    path('listar/', CategoriaList.as_view(), name='listar'),
    path('crear/', CategoriaCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', CategoriaUpdate.as_view(), name='editar'),
    path('eliminar/<int:pk>/', CategoriaDelete.as_view(), name='eliminar'),
]
