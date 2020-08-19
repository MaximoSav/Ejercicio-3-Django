from django.db import models

# Create your models here.


class Biblioteca (models.Model):
    def cargarMateriales(self):
        pass

    def cargarPersonas(self):
        pass

    def __str__(self):
        return ("{}:{}".format(self.cargarMateriales(), self.cargarPersonas()))

class Persona(models.Model):
    tipoPersona = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    correo = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeoudo = models.FloatField()

    def __str__(self):
        return ("{}:{}".format(self.nombre, self.apellido, self.telefono, self.correo))

class Material (models.Model):
    Biblioteca = models.ForeignKey('Biblioteca', on_delete = models.CASCADE,)
    tipoMaterial = models.CharField(max_length = 40)
    codigo = models.CharField(max_length = 40)
    autor = models.CharField(max_length = 40)
    titulo = models.CharField(max_length = 40)
    anio = models.IntegerField()
    status = models.CharField(max_length = 40)

    def __str__(self):
        return ("{}:{}".format(self.autor, self.titulo, self.anio, self.status))

class Prestamo (models.Model):
    persona = models.OneToOneField(Persona, on_delete = models.CASCADE, default = None)
    codigo = models.CharField(max_length = 40)
    id = models.CharField(max_length = 40, primary_key = True)
    fechaSalida = models.CharField(max_length = 40)
    fechaRegreso = models.CharField(max_length = 40)


    def __str__(self):
        return ("{}:{}".format(self.codigo, self.id, self.fechaSalida, self.fechaRegreso))

class Libro (Material):
    editorial = models.CharField(max_length = 40)

    def __str__(self):
        return ("{}:{}".format(self.editorial))

class Revista (Material):
    def asd1(self):
        pass

class Alumno (Persona):
    matricula = models.IntegerField()

    def __str__(self):
        return ("{}:{}".format(self.nombre, self.apellido, self.telefono, self.correo))

class Profesor (Persona):
    numEmpleado = models.IntegerField()

    def __str__(self):
        return ("{}:{}".format(self.nombre, self.apellido, self.telefono, self.correo))