from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import EmailField, CharField, PasswordInput
from django.contrib.auth.models import User

class FormularioRegistroUsuario(UserCreationForm):

   email = EmailField()
   password1 = CharField(label="Contraseña", widget=PasswordInput)
   password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

   class Meta:
      model = User  # Utiliza tu modelo de usuario personalizado
      fields = ["username", "email", "password1", "password2"]
      help_texts = {"username": "", "email": "", "password1": "", "password2": ""}

class FormularioInicioSesion(AuthenticationForm):
   pass

class UserProfileForm(UserChangeForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name', 'email', 'username', 'bio']