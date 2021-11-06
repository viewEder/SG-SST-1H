from django.db import models
from empresa.models import Empleados
from django.db.models import CASCADE

# Create your models here.

class Periodo(models.Model):

    anio = models.CharField(Verbose_name = "Año", max_length= 4, null= False)

    class Meta:
        verbose_name = "Periodo"

    def __str__(self):
        return self.anio

class Cronograma(models.Model):
    # atributos de la clase Cronograma

   periodo = models.OneToOneField(Periodo, on_delete=models.CASCADE)
   nombre_cronograma = models.CharField(verbose_name="Cronograma", max_length=50)
   empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE )
   actividad = models.CharField(verbose_name="Actividad", max_length=100, null = False)
   responsable = models.CharField(verbose_name="Responsable", max_length=250, null = False)
   valor_presupuestado= models.DecimalField(verbose_name="Valor Presupuestado", max_digits= 15, decimal_places= 2)
   observaciones = models.TextField(verbose_name="Observaciones", null = True, blank= True)
   create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
   modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

   class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronogramas" 

   def __str__(self):
        return self.nombre_cronograma

class Ejecucion(models.Model):

    cronograma = models.OneToOneField(Cronograma, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Ejecucion"
        
    def __str__(self):
        return self.periodo
