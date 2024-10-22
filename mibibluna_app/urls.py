from . import views 
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    
    path('empleados/activar/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('empleados/modificar/<int:id>', views.modificar_empleado, name='modificar_empleado'),
    path('empleados/listado', views.listado_empleados, name='listado_empleados'),
    path('empleados/crear', views.agregar_empleado, name='crear_empleado'),

    path('autores/modificar/<int:id>', views.modificar_autor, name="modificar_autor"),
    path('autores/activar/<int:id>', views.activar_autor, name="activar_autor"),
    path('autores/desactivar/<int:id>', views.desactivar_autor, name="desactivar_autor"),
    path('autores/listado', views.listado_autores, name='listado_autores'),
    path('autores/nuevo', views.agregar_autor, name='crear_autor'),

    path('socios/nuevo', views.agregar_socio, name='crear_socio'),
    path('socios/listado', views.listado_socios, name='listado_socios'),
    path('socios/desactivar/<int:id>', views.desactivar_socio, name="desactivar_socio"),
    path('socios/activar/<int:id>', views.activar_socio, name="activar_socio"),
    path('socios/modificar/<int:id>', views.modificar_socio, name="modificar_socio"),

    path('libros/activar/<int:id>', views.activar_libro, name="activar_libro"),
    path('libros/desactivar/<int:id>', views.desactivar_libro, name='desactivar_libro'),
    path('libros/listado', views.listado_libros, name='listado_libros'),
    path('libros/modificar/<int:id>', views.modificar_libro, name="modificar_libro"),
    path('libros/nuevo', views.agregar_libro, name='nuevo_libro'),


    path('prestamos/nuevo', views.agregar_prestamo, name='crear_prestamo'),
    path('prestamos/eliminar/<int:id>', views.eliminar_prestamo, name="eliminar_prestamo"),
    path('prestamos/listado', views.listado_prestamos, name='listado_prestamos'),
    path('prestamos/modificar/<int:id>', views.modificar_prestamo, name='modificar_prestamo'),
]
