# En el archivo forms.py de tu aplicación (miapp)
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
   class Meta:
      model = Libro
      fields = ['titulo', 'autor', 'publicacion']

      widgets = {
         'publicacion': forms.DateInput(attrs={'type': 'date'}),
      }