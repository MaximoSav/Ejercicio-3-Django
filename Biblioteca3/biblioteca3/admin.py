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
    list_display = ['',]


admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(Material, MaterialSup)
admin.site.register(Persona, )
admin.site.register(Prestamo, )
admin.site.register(Alumno, AlumnoSup)
admin.site.register(Profesor, )
admin.site.register(Libro, )
admin.site.register(Revista, )