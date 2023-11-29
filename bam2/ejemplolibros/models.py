# En el archivo models.py de tu aplicación (miapp)
from django.db import models


class Libro(models.Model):
    # Define el modelo Libro con tres campos: título, autor y fecha de publicación
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    publicacion = models.DateField()
    unidades_disponibles = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo
