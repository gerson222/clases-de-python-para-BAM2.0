# En el archivo views.py de tu aplicación (ejemplolibros)
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from .forms import LibroForm

def _manejar_formulario(request, Formulario, template, redireccionar_a):
    """
    Maneja la lógica común de procesamiento de formularios.

    Parameters:
    - request: HttpRequest
    - Formulario: La clase del formulario a manejar.
    - template: La plantilla a renderizar.
    - redireccionar_a: La vista a la cual redirigir después de procesar el formulario.

    Returns:
    - HttpResponse: Redirige a la vista especificada si el formulario es válido, de lo contrario, renderiza el formulario.
    """
    form = Formulario()

    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redireccionar_a)

    return render(request, template, {'form': form})

def listar_libros(request):
    """
    Muestra una lista de libros con opciones de búsqueda y visualización completa.

    Parameters:
    - request: HttpRequest

    Returns:
    - HttpResponse: Renderiza la página 'listar_libros.html' con la lista de libros y opciones de búsqueda.
    """

    # Inicializar el formulario de Libro
    form = LibroForm(request.POST or None)
    # Obtener el término de búsqueda de la URL
    query = request.GET.get('q', '')
    # Manejar la creación de un nuevo libro utilizando la función compartida
    _manejar_formulario(request, LibroForm, 'libros/crear_libros.html', 'listar_libros')
    # Obtener todos los libros de la base de datos
    libros = Libro.objects.all()
    # Filtrar libros por el término de búsqueda si está presente
    if query:
        libros = libros.filter(titulo__icontains=query)
    # Verificar si se debe mostrar todos los libros (sin filtro de búsqueda)
    mostrar_todo = request.GET.get('mostrar_todo', False)
    # Redirigir a la misma vista sin filtro de búsqueda si se solicita mostrar todo
    if mostrar_todo:
        return redirect('listar_libros')
    # Renderizar la página con la lista de libros y el formulario de búsqueda
    return render(request, 'libros/listar_libros.html', {'libros': libros, 'form': form, 'query': query})

def crear_libro(request):
    return _manejar_formulario(request, LibroForm, 'libros/crear_libros.html')

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


#funcion para buscar libros en un html distinto al de muestra de libros de la base de datos
def buscar_libros(request):
    query = request.GET.get('q', '')  # Obtiene el término de búsqueda de la URL
    libros = Libro.objects.filter(titulo__icontains=query)  # Realiza la búsqueda

    return render(request, 'libros/buscar_libros.html', {'libros': libros, 'query': query})