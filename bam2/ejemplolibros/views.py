# En el archivo views.py de tu aplicación (ejemplolibros)
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    form = LibroForm()
    query = request.GET.get('q', '')
    
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')

    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()

    return render(request, 'libros/listar_libros.html', {'libros': libros, 'form': form, 'query': query})

def crear_libro(request):
    return _manejar_formulario(request, LibroForm, 'libros/crear_libros.html')

def _manejar_formulario(request, Formulario, template):
    form = Formulario()

    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')

    return render(request, template, {'form': form})

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

def buscar_libros(request):
    query = request.GET.get('q', '')  # Obtiene el término de búsqueda de la URL
    libros = Libro.objects.filter(titulo__icontains=query)  # Realiza la búsqueda

    return render(request, 'libros/buscar_libros.html', {'libros': libros, 'query': query})