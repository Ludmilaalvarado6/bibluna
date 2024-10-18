class Empleados(models.Model):
    nombre = models.CharField(max_length=38,null=False,default=None)
    apellido = models.CharField(max_length=38,null=False,default=None)
    fecha_Contratacion = models.CharField(max_length=38,null=True,default=None)
    Cargo = models.CharField(max_length=38,null=True,default=None)
    Telefono = models.charField(max_length=38,null=True,default=None)

    def __str__(self) str:
        return f'nombre: {self.nombre} = apellido: {self.apellido} = fecha_Contratacion: {self.fecha_Contratacion} = Cargo: {self.Cargo} = Telefono {self.Telefono}

class Editorial(models.Model):
    nombre = models.CharField(max_length=38,null=False,default=None)
    telefono = models.CharField(max_length=38,null=True,default=None)
    gmail = models.charField(maxlenth=38,null=True,default=None)
    

class Libro(models.Model):
    titulo = models.CharField(max_length=38,null=False,default=None)
    ISBN = models.CharField(max_length,null=False,default=None)
    ano_Publcacion = models.IntegerField(max_length,null=True,default=None)

    def __str__(self) str:
        return f'titulo: {self.titulo} = ISBN {self.ISBN} = ano_Publicacion{self.ano_Publicacion}

class Autores(models.Model)
      nombre = models.CherFied(max_lenhtg=38,null=False,default=None)
      apellido = models.CherFied(max_lenhtg=38,null=False,default=None)
      nacionalidad = models.CherFied(max_lenhtg=38,null=True,default=None)

      def __str__ str:
    return f'nombre {self.nombre} = apellido {self.apellido} = nacionalidad {self.nacionalidad}

    class Prestamos(models.Model)
    fecha_prestamos = models.CherFied(max_lenhtg=38,null=False,default=None)
    fecha_devolucion = models.CherFied(max_lenhtg=38,null=False,default=None)

    def __str__ str:
        return f'fecha_prestamos {self.fecha_prestamos} = fecha_devolucion {self.fecha_devolucion}

class Socios(models.Model)
    nombre = models.CherFied(max_lenhth=38,null=False,default=None)
    apellido = model.CherFied(max_lenhtg=38,null=False,default=None)
    direccion = model.CherFied(max_lenhtg=38,null=True,default=None)
    telefono = model.CherField(max_length=38,null=True,default=None)
    fecha_afiliacion = modelCherField(max_lenhth=38,null=False,default=None)

    def __str__ str: 
        return f'nombre {self.nombre} = apellido {self.apellido} = direccion {self.direccion } = telefono {self.telefono} = fecha_afiliacion {self.fecha_afiliacion}
        




























