from django.contrib import admin
from django.urls import path, include
from ejemplolibros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include("ejemplolibros.urls")),
    path('users/', include("users.urls")),
]
