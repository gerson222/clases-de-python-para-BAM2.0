from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.contrib import messages
from .forms import *


def registrar(request):
   form = FormularioRegistroUsuario(request.POST or None)
   if request.method == "POST":
      if form.is_valid():
         form.save()
         return redirect('iniciar_sesion')
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
            return redirect('profile')
         else:
            form.add_error(None, 'Credenciales no válidas')
   else:
      return render(request, 'user/login.html', {'form': form})
   return render(request, 'user/login.html', {'form': form})

@login_required(login_url='/users/login/')
def cerrar_sesion(request):
   logout(request)
   return redirect('home')

@login_required(login_url='/users/login/')
def profile(request):
   user = request.user
   user_data = model_to_dict(user)
   context = {
      'user_data': user_data,
   }
   return render(request, 'user/profile.html', context)

@login_required(login_url='/users/login/')
def edit_profile(request):
   user = request.user
   if request.method == 'POST':
      form = UserProfileForm(request.POST, instance=user)
      if form.is_valid():
            form.save()
            return redirect('profile')
   else:
      form = UserProfileForm(instance=user)
   context = {
      'form': form,
   }
   return render(request, 'user/edit_profile.html', context)

@login_required(login_url='/users/login/')
def cambiar_contraseña(request):
   user = request.user
   if request.method == 'POST':
      password_form = PasswordChangeForm(user, request.POST)
      if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('profile')
   else:
      password_form = PasswordChangeForm(user)
   context = {
      'password_form': password_form,
   }
   return render(request, 'user/cambiar_contraseña.html', context)