# En el archivo views.py de tu aplicación (ejemplolibros)
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    libros = Libro.objects.all()
    form = LibroForm()

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
        else:
            form = LibroForm()
    return render(request, 'libros/listar_libros.html', {'libros': libros, 'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libros.html', {'form': form})

def modificar_libro(request, id):
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
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')

    return render(request, 'libros/borrar_libro.html', {'libro': libro})