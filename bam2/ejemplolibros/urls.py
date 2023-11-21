# En el archivo urls.py de tu aplicación (miapp)
from django.urls import path
from .views import borrar_libro, listar_libros, crear_libro, modificar_libro

urlpatterns = [
    # Configura la URL libros/ que mapea a la vista listar_libros
    path('libros/', listar_libros, name='listar_libros'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/modificar/<int:id>/', modificar_libro, name='modificar_libro'),
    path('libros/borrar/<int:id>/', borrar_libro, name='borrar_libro'),
]