from django.contrib import admin
from .models import Profesor, Alumno, Evaluacion, Asistencia, Nota

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Evaluacion)

admin.site.register(Asistencia)
admin.site.register(Nota)


