from django.db import models

# Create your models here.

class sobremi(models.Model):
    pk_sobremi = models.AutoField(primary_key=True)
    nombre = models.CharField('mi nombre', max_length=50, blank=False, null=False)
    direccion = models.CharField('mi direccion', max_length=300, blank=False, null=False)
    telefono = models.CharField('telefono de contacto', max_length=8, blank=False, null=False)
    correo = models.EmailField('correo de contacto',blank=False, null=False)
    descripcion = models.TextField('Breve descripcion de mi persona',blank=False, null=False)
    foto = models.URLField('Foto de mi persona', blank=False, null=False)

class experiencia(models.Model):
    pk_experiencia = models.AutoField(primary_key=True)
    puesto = models.CharField('puesto funcional', max_length=150, blank=False, null=False)
    empresa = models.CharField('empresa donde trabaje', max_length=150, blank=False, null=False)
    descripcion = models.TextField('desempeño dentro de la empresa',blank=False, null=False)
    fecha_inicio = models.DateField('fecha de inicio laboral', blank=False, null=False)
    fecha_salida = models.DateField('fecha de finalizacion laboral', blank=False, null=False)

class educacion(models.Model):
    pk_educacion = models.AutoField(primary_key=True)
    establecimiento = models.CharField('establecimiento donde se obtuvo', max_length=150, blank=False, null=False)
    titulo = models.CharField('titulo conseguido', max_length=150, blank=False, null=False)
    descripcion = models.TextField('desempeño del titulo',blank=False, null=False)
    promedio = models.IntegerField('Mi promedio obtenido', blank=False, null=False)
    fecha_inicio = models.DateField('fecha de inicio preparacion academica', blank=False, null=False)
    fecha_salida = models.DateField('fecha de finalizacion preparacion academica', blank=False, null=False)

class icono(models.Model):
    pk_icono = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre icono', max_length=50, blank=False, null=False)
    estructura = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.estructura

class desempeno(models.Model):
    pk_desempeno = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=False, null=False)

class interes(models.Model):
    pk_interes = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=False, null=False)

class reconocimiento(models.Model):
    pk_reconocimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, blank=False, null=False)