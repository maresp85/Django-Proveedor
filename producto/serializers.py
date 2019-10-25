from rest_framework import serializers
from .models import Producto
from categoria.serializers import CategoriaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria_id = CategoriaSerializer(many=False)

    class Meta:
        model = Producto
        fields = ('id', 'categoria_id', 'descripcion', 'precio_unitario', 'cantidad')

class ProductoSerializerP(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('categoria_id', 'descripcion', 'precio_unitario', 'cantidad')
