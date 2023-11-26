# En el archivo forms.py de tu aplicación (miapp)
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
   mostrar_todo = forms.CharField(required=False, widget=forms.HiddenInput())
   class Meta:
      model = Libro
      fields = ['titulo', 'autor', 'publicacion']

      widgets = {
         'titulo': forms.TextInput(attrs={'class': 'input-titulo'}),
         'autor': forms.TextInput(attrs={'class': 'input-autor'}),
         'publicacion': forms.DateInput(attrs={'type': 'date', 'class': 'input-publicacion'}),
      }

   labels = {
      'titulo': 'Título',
      'autor': 'Autor',
      'publicacion': 'Fecha de Publicación',
   }
