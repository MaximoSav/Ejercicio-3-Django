from django.contrib import admin
from .models import *
# Register your models here.

class BibliotecaAdmin (admin.ModelAdmin):
    class EntryInLinesRevista(admin.TabularInline):
        model = Revista
    class EntryInLinesLibro(admin.TabularInline):
        model = Libro

    inlines = [EntryInLinesRevista]
    inlines = [EntryInLinesLibro]


class AlumnoSup(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'telefono', 'correo', 'matricula', 'numLibros']

class MaterialSup(admin.ModelAdmin):
    list_display = ['autor', 'titulo', 'anio', 'tipoMaterial']


class PersonaSup (admin.ModelAdmin):
    list_display = ['nombre','apellido','correo','telefono']

class PrestamoSup(admin.ModelAdmin):
    list_display = ['persona','codigo','fechaSalida','fechaRegreso']

class ProfesorSup(admin.ModelAdmin):
    list_display = ['nombre','apellido','correo','telefono','numEmpleado']

class LibroSup(admin.ModelAdmin):
    list_display = ['Biblioteca','autor','titulo','anio','status','fotoPortada']

class RevistaSup(admin.ModelAdmin):
    list_display = ['Biblioteca','autor','titulo','anio','status']

admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(Material, MaterialSup)
admin.site.register(Persona, PersonaSup)
admin.site.register(Prestamo, PrestamoSup)
admin.site.register(Alumno, AlumnoSup)
admin.site.register(Profesor, ProfesorSup)
admin.site.register(Libro, LibroSup)
admin.site.register(Revista, RevistaSup)