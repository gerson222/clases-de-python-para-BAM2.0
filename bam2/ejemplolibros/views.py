# En el archivo views.py de tu aplicación (ejemplolibros)
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    """
    Muestra una lista de todos los libros en la base de datos.

    Parameters:
    - request: HttpRequest

    Returns:
    - HttpResponse: Renderiza la página 'listar_libros.html' con la lista de libros.
    """
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def crear_libro(request):
    """
    Permite la creación de un nuevo libro mediante un formulario.

    Parameters:
    - request: HttpRequest

    Returns:
    - HttpResponse: Renderiza la página 'crear_libros.html' con el formulario de creación de libros.
    """
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libros.html', {'form': form})

def modificar_libro(request, id):
    """
    Permite la modificación de un libro existente mediante un formulario.

    Parameters:
    - request: HttpRequest
    - id: int, ID del libro a modificar.

    Returns:
    - HttpResponse: Renderiza la página 'modificar_libro.html' con el formulario prellenado del libro a modificar.
    """
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/modificar_libro.html', {'form': form})

def borrar_libro(request, id):
    """
    Permite la eliminación de un libro existente.

    Parameters:
    - request: HttpRequest
    - id: int, ID del libro a eliminar.

    Returns:
    - HttpResponse: Renderiza la página 'borrar_libro.html' para confirmar la eliminación del libro.
    """
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')

    return render(request, 'libros/borrar_libro.html', {'libro': libro})