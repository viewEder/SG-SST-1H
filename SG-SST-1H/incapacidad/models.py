from django.db import models
from core.types.meses import Meses
from django.db.models.deletion import CASCADE
from empresa.models import Empleados



# Create your models here.

class Ausentismo(models.Models):
    mes = models.CharField(max_length=20, choices= Meses,verbose_name="Periodo", null=True, blank=True)
    nombre_completo = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    #salario dia
    codigo_enfermedad = models.CharField(max_length = 15, verbose_name = "Codigo de la enfermedad", null = False)
    diagnostico = models.CharField(max_length = 250, verbose_name = "Diagnostico", null = False)
    grupo_dx = models.CharField(max_length = 100, verbose_name = "Grupo DX", null = False)
    segmento_osteomuscular = models.CharField(max_length = 100, verbose_name = "Codigo de la enfermedad", null = False)
    orgien = models.CharField(max_length = 50, verbose_name = "Origen de la enfermedad", null = False)
    clasificacion = models.CharField(max_length = 50, verbose_name = "Clasificación de la enfermedad", null = False)
    fecha_inicio = models.DateField(verbose_name = "Fecha de de inicio", auto_now = False, auto_now_add = False)
    fecha_finalizacion = models.DateField(verbose_name = "Fecha de finalizacion", auto_now = False, auto_now_add = False)
    total_incapacidad = models.CharField(max_length = 5, verbose_name = "Total dias de incapacidad", null = False)
    #valor incapacidad
    #valor asumido por la empresa
    #Valor asumido por eps

    
    



   
    


    




