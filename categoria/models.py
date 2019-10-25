from django.db import models

# Categorias de los productos.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.descripcion)
