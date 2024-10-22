from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=38,null=False)
    apellido = models.CharField(max_length=38,null=False)
    legajo= models.IntegerField(verbose_name='Legajo')
    activo= models.BooleanField(default=True,verbose_name='Activo')

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Editorial(models.Model):
    nombre = models.CharField(max_length=38,null=False)
    telefono = models.CharField(max_length=38,null=True,default=None)
    email = models.EmailField(max_length=38,null=True,default=None)
    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name_plural = "Editoriales"
        
class Autor(models.Model):
    nombre = models.CharField(max_length =38,null=False)
    apellido = models.CharField (max_length =38,null=False)
    nacionalidad = models.CharField (max_length =38,null=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    class Meta:
        verbose_name_plural = 'Autores'

class Libro(models.Model):
    titulo = models.CharField(max_length=38,null=False)
    isbn = models.CharField(max_length=30,null=False)
    ano_publicacion = models.IntegerField(null=True,verbose_name='Año de Publicación')
    autor = models.ForeignKey(
        Autor,  
        related_name='autores_libros',
        on_delete=models.CASCADE,
        verbose_name='Autor',
    ) 
    activo = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return self.titulo


class Socio(models.Model):
    nombre = models.CharField (max_length=38,null=False)
    apellido = models.CharField (max_length =38,null=False)
    direccion = models.CharField (max_length =38,null=True)
    telefono = models.CharField(max_length=38,null=True)
    activo= models.BooleanField(default=True,verbose_name='Activo')

    def __str__(self): 
        return f'{self.apellido}, {self.nombre}'
        
 
class Prestamo(models.Model):
    fecha_retiro = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True)
    socio= models.ForeignKey(Socio,
                             related_name='prestamos',
                             on_delete=models.PROTECT) 
    # Protect evita que se elimine un socio si existe un prestamo asiado a él
    libro= models.ForeignKey(Libro,
                             related_name='libros',
                             on_delete=models.PROTECT)
    # Protect evita que se elimine un Libro si existe un prestamo asiado a él
    empleado= models.ForeignKey(Empleado,
                                related_name='prestamos_realizados',
                                on_delete=models.PROTECT)
    def __str__(self):
        return str(self.id) 