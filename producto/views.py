from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Producto
from categoria.models import Categoria
#imports para el apirest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer, ProductoSerializerP

# Listado de registros del modelo Categoria
class ProductoList(ListView):
    model = Producto

# Crear un nuevo Producto
class ProductoCreate(CreateView):
    model = Producto
    success_url = reverse_lazy('producto:listar')
    fields = ['descripcion', 'precio_unitario', 'cantidad', 'categoria']

    def get_success_url(self):
        producto = Producto.objects.get(id=self.object.id)
        producto.cantidad = 999
        producto.save()
        messages.add_message(self.request, messages.SUCCESS, "Producto creado satisfactoriamente")
        return reverse_lazy('producto:listar')

# Crear un nuevo Producto
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:listar')

#API CRUD para los Productos
class ProductosAPI(APIView):
    #muestra información de todos los productos
    def get(self, request):
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductoSerializerP(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializerP(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
