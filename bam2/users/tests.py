from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UsuarioTest(TestCase):

   def setUp(self):
      self.client = Client()
      self.registro_url = reverse('registrar')
      self.iniciar_sesion_url = reverse('login')
      self.llegaste_url = reverse('llegaste')
      self.user_data = {'username': 'testuser', 'password1': 'testpassword123', 'password2': 'testpassword123'}

   def test_registrar_usuario_get(self):
      response = self.client.get(self.registro_url)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'user/registro.html')

   def test_registrar_usuario_post_exitoso(self):
      response = self.client.post(self.registro_url, self.user_data)
      self.assertEqual(response.status_code, 302)  # Redirigido después de un registro exitoso
      self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

   def test_registrar_usuario_post_invalido(self):
      response = self.client.post(self.registro_url, {'username': 'testuser'})
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'user/registro.html')
      self.assertContains(response, 'Formulario NO valido')

   def test_iniciar_sesion_get(self):
      response = self.client.get(self.iniciar_sesion_url)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'user/login.html')

   def test_iniciar_sesion_post_exitoso(self):
      # Crea un usuario para la prueba
      User.objects.create_user(username='testuser', password='testpassword123')

      response = self.client.post(self.iniciar_sesion_url, {'username': 'testuser', 'password': 'testpassword123'})
      self.assertEqual(response.status_code, 302)  # Redirigido después de un inicio de sesión exitoso
      user = User.objects.get(username='testuser')
      self.assertTrue(user.is_authenticated)

   def test_iniciar_sesion_post_invalido(self):
      response = self.client.post(self.iniciar_sesion_url, {'username': 'testuser', 'password': 'wrongpassword'})
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'user/login.html')
      self.assertContains(response, 'Credenciales no válidas')

   def test_llegaste_usuario_autenticado(self):
      # Crea un usuario para la prueba
      User.objects.create_user(username='testuser', password='testpassword123')

      # Inicia sesión
      self.client.login(username='testuser', password='testpassword123')

      response = self.client.get(self.llegaste_url)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'user/logeo.html')

   def test_llegaste_usuario_no_autenticado(self):
      response = self.client.get(self.llegaste_url)
      self.assertEqual(response.status_code, 302)  # Redirigido al inicio de sesión
