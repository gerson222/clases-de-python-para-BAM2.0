from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

def registrar(request):
   form = FormularioRegistroUsuario(request.POST or None)

   if request.method == "POST":
      if form.is_valid():
         form.save()
         return redirect('iniciar_sesion')
   
   # Asegúrate de pasar el formulario vacío en el caso de una solicitud GET
   return render(request, "user/registro.html", {"form": form})

def iniciar_sesion(request):
   form = FormularioInicioSesion(request, data=request.POST or None)
   if request.method == 'POST':
      if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
            auth_login(request, user)
            return redirect('llegaste')
         else:
            form.add_error(None, 'Credenciales no válidas')
   else:
      return render(request, 'user/login.html', {'form': form})

@login_required
def cerrar_sesion(request):
   # Cierra la sesión del usuario
   logout(request)
   # Redirige a la página de inicio o a donde desees después del logout
   return redirect('navbar')

@login_required
def llegaste(request):
   return render(request, 'user/logeo.html')
