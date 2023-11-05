from django.contrib import admin
from .models import *


# Register your models here.

class SobremiAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')

admin.site.register(sobremi, SobremiAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('puesto', 'empresa', 'fecha_inicio', 'fecha_salida')

admin.site.register(experiencia, ExperienciaAdmin)

class EducacionAdmin(admin.ModelAdmin):
    list_display = ('establecimiento', 'titulo', 'promedio', 'fecha_salida')

admin.site.register(educacion, EducacionAdmin)

class IconoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(icono, IconoAdmin)

class DesmpenoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

admin.site.register(desempeno, DesmpenoAdmin)

class InteresAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

admin.site.register(interes, InteresAdmin)

class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(reconocimiento, ReconocimientoAdmin)