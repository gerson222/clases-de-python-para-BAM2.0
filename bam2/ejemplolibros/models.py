# En el archivo models.py de tu aplicación (miapp)
from django.db import models


class Libro(models.Model):
    # Define el modelo Libro con tres campos: título, autor y fecha de publicación
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    publicacion = models.DateField()

    def __str__(self):
        return self.titulo
