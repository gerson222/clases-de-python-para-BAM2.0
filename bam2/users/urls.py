from django.urls import path
from .views import *

urlpatterns = [
   path("registrar/", registrar, name="registrar"),
   path("login/", iniciar_sesion, name='login'),
   path("profile/", profile, name='profile'),
   path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
   path('edit_profile/', edit_profile, name='edit_profile'),
   path('cambiar_contraseña/', cambiar_contraseña, name='cambiar_contraseña'),
]