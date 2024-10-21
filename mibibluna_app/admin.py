from django.contrib import admin

from .models import Empleado, Editorial, Autor, Libro, Socio, Prestamo

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = 'id','nombre', 'apellido', 'legajo', 'activo'
    search_fields = 'nombre', 'apellido'
    list_filter = 'activo',

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = 'id','nombre', 'telefono', 'email'
    search_fields = 'nombre',

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = 'id','nombre', 'apellido', 'nacionalidad', 'activo'
    search_fields = 'nombre', 'apellido', 'nacionalidad'
    list_filter = 'activo',

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = 'id','titulo', 'ISBN', 'ano_publicacion', 'autor', 'activo'
    search_fields = 'titulo', 'ISBN'
    list_filter = 'activo', 'autor'

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = 'id','nombre', 'apellido', 'direccion', 'telefono'
    search_fields = 'nombre', 'apellido'
    
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = 'id','fecha_retiro', 'fecha_devolucion', 'socio', 'libro', 'empleado'
    list_filter = 'socio', 'libro', 'empleado'