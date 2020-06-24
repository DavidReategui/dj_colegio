from django.contrib import admin
from .models import Profesor, Alumno, Evaluacion, Asistencia, Nota

# Register your models here.
# Falta 

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']
    search_fields = ['name','last_name']

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha','alumno','asiste','Justificacion']
    search_fields = ['alumno__name']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']
    search_fields = ['name','last_name']

class NotasAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha','alumno', 'evaluacion','nota']
    search_fields = ['alumno__name']
    
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Evaluacion)

admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Nota, NotasAdmin)


