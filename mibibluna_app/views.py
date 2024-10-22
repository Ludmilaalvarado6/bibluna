from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from mibibluna_app.models import Autor, Empleado, Libro, Prestamo, Socio
from django.utils import timezone


def index(request ):
    return render (request,'mibibluna_app\index.html')

def activar_empleado(request,id):
    empleado = get_object_or_404(Empleado,id=id)
    if empleado.activo:
        response_data = { 
            "status": "info",
            "mensaje": f"El empleado {empleado.nombre} {empleado.apellido} ya esta activo."
        }
        return JsonResponse(response_data)
    else:
        empleado.activo = True
        empleado.save()
        return redirect('listado_empleados')

def desactivar_empleado(request,id):
    empleado = get_object_or_404(Empleado, id=id)
    if empleado.activo:
        empleado.activo = False
        empleado.save()
        return redirect('listado_empleados')
    else:
        response_data = { 
            "status": "info",
            "mensaje": f"El empleado {empleado.nombre} {empleado.apellido} ya se encontraba desactivado."
        }
        return JsonResponse(response_data)

def modificar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    context = {"empleado" : empleado}
    if request.POST:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        legajo = request.POST["legajo"]
        activo = True if request.POST.get("activo") else False

        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.legajo = legajo
        empleado.activo = activo
        empleado.save()
        return redirect('listado_empleados')
    return render(request, 'mibibluna_app/modificar_empleado.html', context)

def listado_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        "empleados" : empleados
    }
    return render(request, 'mibibluna_app/listado_empleados.html', context)

def agregar_empleado(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        legajo = request.POST['legajo']

        Empleado.objects.create(
            nombre = nombre,
			apellido = apellido,
            legajo = legajo,
        )
        return redirect('listado_empleados')
    return render(request, 'mibibluna_app/agregar_empleado.html')

# autor

def modificar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.POST:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        nacionalidad = request.POST["nacionalidad"]
        activo = True if request.POST.get("activo") else False
        autor.nombre = nombre
        autor.apellido = apellido
        autor.nacionalidad = nacionalidad
        autor.activo = activo
        autor.save()
        return redirect('listado_autores')
    return render(request, 'mibibluna_app/modificar_autor.html', { "autor": autor })

def activar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.activo = True
    autor.save()
    return redirect('listado_autores')

def desactivar_autor(request,id):
    autor = get_object_or_404(Autor, id=id)

    if autor.activo:
        autor.activo = False
        autor.save()
        return redirect('listado_autores')
    else:
        response_data = { 
            "status": "info",
            "mensaje": f"El autor {autor.nombre} {autor.apellido} ya se encontraba desactivado."
        }
        return JsonResponse(response_data)
    
def agregar_autor(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        nacionalidad = request.POST['nacionalidad']

        Autor.objects.create(
            nombre = nombre,
			apellido = apellido,
            nacionalidad = nacionalidad,
        )
        return redirect('listado_autores')
    return render(request, 'mibibluna_app/agregar_autor.html')    

def listado_autores(request):
    autores= Autor.objects.all()
    context= {'autores':autores}
    return render(request, 'mibibluna_app/listado_autores.html', context)


# socio

def agregar_socio(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']

        Socio.objects.create(
            nombre = nombre,
			apellido = apellido,
            direccion = direccion, 
            telefono = telefono
        )
        return redirect('listado_socios')

    return render(request, 'mibibluna_app/agregar_socio.html')

def listado_socios(request):
    socios = Socio.objects.all()
    return render(request, 'mibibluna_app/listado_socios.html', { "socios": socios })

def desactivar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.activo = False
    socio.save()
    return redirect('listado_socios')

def activar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.activo = True
    socio.save()
    return redirect('listado_socios')

def modificar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    if request.POST:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        activo = True if request.POST.get("activo") else False

        socio.nombre = nombre
        socio.apellido = apellido
        socio.direccion = direccion
        socio.telefono = telefono
        socio.activo = activo

        socio.save()
        return redirect('listado_socios')
    return render(request, 'mibibluna_app/modificar_socio.html', { "socio": socio })


# Libro

def listado_libros(request):
    libros= Libro.objects.all()
    context= {'libros':libros}
    return render(request, 'mibibluna_app/listado_libros.html', context)

def activar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.activo = True
    libro.save()
    return redirect('listado_libros')

def desactivar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.activo = False
    libro.save()
    return redirect('listado_libros')


def modificar_libro(request, id):
    autores = Autor.objects.filter(activo=True)
    libro = get_object_or_404(Libro, id=id)
    context = {
        "autores":autores,
        "libro":libro
    }

    if request.POST:
        titulo = request.POST["titulo"]
        ano_publicacion = request.POST["ano_publicacion"]
        isbn = request.POST["isbn"]
        autor = request.POST["autor"]
        activo = True if request.POST.get("activo") else False

        libro.titulo = titulo
        libro.ano_publicacion = ano_publicacion
        libro.isbn = isbn
        libro.autor_id = autor
        libro.activo = activo

        libro.save()

        return redirect('listado_libros')

    return render(request, 'mibibluna_app/modificar_libro.html', context)

def agregar_libro(request):
    autores = Autor.objects.all()
    context= {
        'autores':autores
    }
    if request.POST:
        titulo = request.POST['titulo']
        ano_publicacion  = request.POST['ano_publicacion']
        isbn = request.POST['isbn']
        autor_id= request.POST['autor']

        Libro.objects.create(
            titulo = titulo,
			ano_publicacion = ano_publicacion,
            isbn = isbn,
            autor_id=autor_id
        )
        return redirect('listado_libros')
    return render(request, 'mibibluna_app/agregar_libro.html',context)


# prestamos


def agregar_prestamo(request):
    socios_activos = Socio.objects.filter(activo=True)
    libros_disponibles = Libro.objects.filter(activo=True)
    empleados_activos = Empleado.objects.filter(activo= True)
    context = {
        'socios': socios_activos,
        'libros': libros_disponibles,
        'empleados': empleados_activos
    }
    if request.method == 'POST':
        
        # Se recopilan los objetos enviados por template
        socio = get_object_or_404(Socio, id = request.POST.get('socio'))
        libro = get_object_or_404(Libro, id = request.POST.get('libro'))
        empleado = get_object_or_404(Empleado, id = request.POST.get('empleado'))

        # Se crea una instancia de prestamos
        prestamo = Prestamo()

        # Se genera automaticamente las fechas

        prestamo.fecha_devolucion = timezone.now() + timezone.timedelta(days=2)
        # Se asignan los objetos enviados
        prestamo.socio = socio
        prestamo.libro = libro
        prestamo.empleado = empleado

        # Se guarda el registro de prestamo creado.
        prestamo.save()

        # Se desactiva el libro prestado hasta que se lo regrese.
        libro.activo = False
        libro.save()

        # Se redirecciona hacia el listado
        return redirect('listado_prestamos')

    # Si no hay libros disponibles, no permitira crear nuevos prestamos.
    if libros_disponibles.count() == 0:
        return JsonResponse({'status': 'info', 'message': 'Lo sentimos, no hay libros disponibles en la biblioteca'})
    return render(request, 'mibibluna_app/agregar_prestamo.html', context)

def eliminar_prestamo(request, id):
    prestamo = Prestamo.objects.get(id=id)
    libro = Libro.objects.get(id=prestamo.libro.id)  #Se recupera el ID del libro prestado para posteriormente activarlo
    prestamo.delete() #Se borra el registro del prestamo
    libro.activo = True     #Se activa el libro prestado
    libro.save()
    return HttpResponse(f'El prestamo con ID {id} fue eliminado.')

def listado_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'mibibluna_app/listado_prestamos.html', { "prestamos": prestamos })

def modificar_prestamo(request,id):
    # Se filtran los registros para enviar solo objetos activos
    socios = Socio.objects.filter(activo=True)
    libros = Libro.objects.filter(activo=True)
    empleados = Empleado.objects.filter(activo= True)
    prestamo= get_object_or_404(Prestamo, id=id)
    libro_prestado= Libro.objects.get(id=prestamo.libro_id)
    
    context = {
        'prestamo': prestamo,
        'socios': socios,
        'libro_prestado': libro_prestado,
        'libros': libros,
        'empleados': empleados
    }

    if request.method == 'POST':
        socio_id = request.POST['socio']
        libro_id = request.POST['libro']
        empleado_id = request.POST['empleado']        
        prestamo.fecha = timezone.now()
        prestamo.devolucion = prestamo.fecha + timezone.timedelta(days=2)
        prestamo.socio_id = socio_id 
        prestamo.libro_id = libro_id  
        prestamo.empleado_id = empleado_id
        prestamo.save() 
        
        if libro_prestado.id != libro_id:
            libro_nuevo= Libro.objects.get(id=prestamo.libro_id)
            libro_prestado.activo = True 
            libro_prestado.save()
            libro_nuevo.activo = False
            libro_nuevo.save()
        return redirect('listado_prestamos')
    return render(request, 'mibibluna_app/modificar_prestamo.html', context)
