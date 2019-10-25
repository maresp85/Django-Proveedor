from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Categoria

# Listado de registros del modelo Categoria
class CategoriaList(ListView):
    model = Categoria

# Crear una nueva Categoria
class CategoriaCreate(CreateView):
    model = Categoria
    success_url = reverse_lazy('categoria:listar')
    fields = ['descripcion']

#Actualizar una categoría
class CategoriaUpdate(UpdateView):
    model = Categoria
    success_url = reverse_lazy('categoria:listar')
    fields = ['descripcion']

#Eliminar una categoría
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria:listar')
