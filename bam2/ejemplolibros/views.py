# En el archivo views.py de tu aplicación (ejemplolibros)
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'ejemplolibros/listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'ejemplolibros/crear_libros.html', {'form': form})

def modificar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'ejemplolibros/modificar_libro.html', {'form': form})

def borrar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')

    return render(request, 'ejemplolibros/borrar_libro.html', {'libro': libro})