from django.urls import path
from .views import *

urlpatterns = [
   path("registrar/", registrar, name="registrar"),
   path("login/", iniciar_sesion, name='login'),
   path("llegaste/", llegaste, name='llegaste'),
]