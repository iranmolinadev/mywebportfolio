from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    modelosobremi = sobremi.objects.all()
    modelexperiencia = experiencia.objects.all()
    modeleducacion = educacion.objects.all()
    modelicon = icono.objects.all()
    modeldesempeno = desempeno.objects.all()
    modelinteres = interes.objects.all()
    modelreconocimiento = reconocimiento.objects.all()
    return render(request, 'index.html', {'modelosobremi':modelosobremi,
                                          'modelexperiencia':modelexperiencia,
                                          'modeleducacion':modeleducacion,
                                          'modelicon':modelicon,
                                          'modeldesempeno':modeldesempeno,
                                          'modelinteres':modelinteres,
                                          'modelreconocimiento':modelreconocimiento})