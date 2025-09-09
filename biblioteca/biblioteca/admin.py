from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible')
    list_filter = ('disponible', 'fecha_publicacion')
    search_fields = ('titulo',)
