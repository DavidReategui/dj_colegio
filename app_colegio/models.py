from django.db import models

# Create your models here.
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['name']

    def __str__(self):
        return self.name

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, blank=False)
    asiste = models.BooleanField(verbose_name='Asistío', default=True)
    Justificacion = models.CharField(max_length=200, blank=True, null=True) 

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['fecha','alumno_id']
        

    #def __str__(self):
    #    return self.name

class Evaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    evaluacion = models.CharField(max_length=30, blank=False, null=False)
    estado = models.BooleanField(verbose_name='Estado', default=True)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'
        ordering=['evaluacion']
        

    def __str__(self):
        return self.evaluacion

class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    evaluacion_id = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    nota = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        

    #def __str__(self):
    #    return self.evaluacion