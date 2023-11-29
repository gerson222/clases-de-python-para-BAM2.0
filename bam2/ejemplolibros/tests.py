from django.test import TestCase, Client
from django.urls import reverse
from .models import Libro
from .forms import LibroForm

class LibroViewsTest(TestCase):
   def setUp(self):
      self.client = Client()

   def test_listar_libros(self):
      response = self.client.get(reverse('listar_libros'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/listar_libros.html')

   def test_crear_libro(self):
      response = self.client.get(reverse('crear_libro'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/crear_libros.html')

      # Prueba la creación de un libro
      libro_data = {
         'titulo': 'Nuevo Libro',
         'autor': 'Autor',
         'publicacion': '2023-01-01',
         'unidades_disponibles': 10,
         'precio': 19.99,
      }
      response = self.client.post(reverse('crear_libro'), libro_data, follow=True)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/listar_libros.html')
      self.assertContains(response, 'Nuevo Libro')

   def test_modificar_libro(self):
      # Crea un libro de prueba
      libro = Libro.objects.create(
         titulo='Libro de Prueba',
         autor='Autor',
         publicacion='2023-01-01',
         unidades_disponibles=5,
         precio=15.99,
      )

      response = self.client.get(reverse('modificar_libro', args=[libro.id]))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/modificar_libro.html')

      # Prueba la modificación del libro
      nuevo_data = {
         'titulo': 'Libro Modificado',
         'autor': 'Nuevo Autor',
         'publicacion': '2023-02-01',
         'unidades_disponibles': 8,
         'precio': 25.99,
      }
      response = self.client.post(reverse('modificar_libro', args=[libro.id]), nuevo_data, follow=True)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/listar_libros.html')
      self.assertContains(response, 'Libro Modificado')

   def test_buscar_libros(self):
      # Crea algunos libros de prueba
      Libro.objects.create(
         titulo='Libro1',
         autor='Autor1',
         publicacion='2023-01-01',
         unidades_disponibles=10,
         precio=19.99,
      )
      Libro.objects.create(
         titulo='Libro2',
         autor='Autor2',
         publicacion='2023-01-02',
         unidades_disponibles=5,
         precio=14.99,
      )

      response = self.client.get(reverse('buscar_libros'), {'q': 'Libro1'})
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/buscar_libros.html')
      self.assertContains(response, 'Libro1')
      self.assertNotContains(response, 'Libro2')

   def test_borrar_libro(self):
      # Crea un libro de prueba
      libro = Libro.objects.create(
         titulo='Libro a Eliminar',
         autor='Autor',
         publicacion='2023-01-01',
         unidades_disponibles=15,
         precio=29.99,
      )

      response = self.client.get(reverse('borrar_libro', args=[libro.id]))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/borrar_libro.html')

      # Prueba la eliminación del libro
      response = self.client.post(reverse('borrar_libro', args=[libro.id]), follow=True)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'libros/listar_libros.html')
      self.assertNotContains(response, 'Libro a Eliminar')
