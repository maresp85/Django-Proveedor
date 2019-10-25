from django.db import models

from categoria.models import Categoria
import datetime

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=200, help_text="Nombre del producto")
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=0, help_text="Precio")
    fecha = models.DateField(default=datetime.date.today)
    cantidad = models.IntegerField(help_text="Cantidad")
    categoria = models.ForeignKey(Categoria, null=False, blank=True, on_delete=models.CASCADE, related_name='categoria')

    def __str__(self):
        return '{}'.format(self.descripcion)
