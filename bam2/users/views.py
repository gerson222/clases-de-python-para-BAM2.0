from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login

def registrar(request):
   if request.method == "POST":
      form = FormularioRegistroUsuario(request.POST)
      if form.is_valid():
         form.save()
         return redirect('iniciar_sesion')
      else:
         return render(request, "user/registro.html", {"form": form, "error": "formulario no valido"})
   else:
      form = FormularioRegistroUsuario()
      return render(request, "user/registro.html", {"form": form})

def iniciar_sesion(request):
   if request.method == 'POST':
      form = FormularioInicioSesion(request, data=request.POST)
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

def llegaste(request):
   return render(request, 'user/logeo.html')
