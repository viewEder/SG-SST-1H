from django.db import models
from cronograma.models import Periodo
from django.db.models.deletion import CASCADE

# Create your models here.

#Modelo Plan Anual
class PlanAnual (models.Model):

    anio= models.ForeignKey(Periodo, on_delete=models.CASCADE )
    objetivo = models.TextField(verbose_name="Objetivo", max_length=250, null = False)
    metas = models.TextField(verbose_name="Metas", max_length=500, null = False)
    alcance = models.TextField(verbose_name="Alcance", max_length=250, null = False)
    activ_planeadas = models.DecimalField(verbose_name="Actividades Planeadas", max_digits= 3)
    activ_cumplidas = models.DecimalField(verbose_name="Actividades Cumplidas", max_digits= 3)
    activ_NoCumplidas = models.DecimalField(verbose_name="Actividades No Cumplidas", max_digits= 3)
    nombre_archivo = models.CharField(verbose_name="Nombre del Archivo", max_length=100, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = "Plan Anual"

    def __str__(self):
        return self.nombre_archivo

#Modelo Equipo Responsable
class EquipoResponsable(models.Model):

    nombre_equipo = models.CharField(verbose_name="Nombre del Equipo", max_length=60, null = False)

    class Meta:
        verbose_name = "Equipo Responsable"
        verbose_name_plural = "Equipos Responsables" 

    def __str__(self):
        return self.nombre_equipo

# Modulo Estructura SGSST
class EstructuraSGSST(models.Model):

    nombre = models.CharField(verbose_name="Nombre", max_length=60, null = False)
    abreviatura = models.CharField(verbose_name="Abreviatura", max_length=10, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = "Estructura SGSST"
        verbose_name_plural = "Estructuras SGSST" 

    def __str__(self):
        return self.nombre

# Modulo Actividades Plan
class ActividadesPlan(models.Model):

    id_plan = models.ForeignKey(PlanAnual, on_delete=models.CASCADE )
    id_estructura = models.ForeignKey(EstructuraSGSST, on_delete=models.CASCADE)
    etapa_PHVA = models.CharField(verbose_name="Etapa PHVA", max_length=250, null = False)
    actividad = models.TextField(verbose_name="Actividad", max_length=500, null = False)
    id_responsable = models.ForeignKey(EquipoResponsable, on_delete=models.CASCADE)
    recursos = models.TextField(verbose_name="Recursos", max_length=60, null = False)
    periocidad = models.CharField(verbose_name="Periocidad", max_length=50, null = False)
    fecha_planeacion = models.DateField(verbose_name="Fecha de Planeación", null=True)
    fecha_cumplimiento = models.DateField(verbose_name="Fecha de Cumplimiento", null=True)
    estado_actividad = models.DecimalField(verbose_name="Estado de la Actividad", max_digits= 3)
    nombre_archivo = models.CharField(verbose_name="Nombre del archivo", max_length=10, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name_plural = "Plan de Actividades"

    def __str__(self):
        return self.actividad

#Modelo Cumplimiento de las Actividades
class CumplimientoActividades(models.Model):

    id_actividad = models.ForeignKey(ActividadesPlan, on_delete=models.CASCADE )
    #mes
    #porcentaje de cumplimiento
    nombre_archivo = models.CharField(verbose_name="Nombre del Archivo", max_length=60, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Cumplimiento de la actividad"
        verbose_name_plural = "Cumplimiento de las actividades" 

    def __str__(self):
        return self.nombre_archivo
