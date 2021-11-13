from django.db import models
from empresa.models import Empleados
from proveedores.models import Proveedores
from django.db.models import CASCADE

# Create your models here.

class Periodo(models.Model):

    anio = models.CharField(verbose_name = "Año", max_length= 4, null= False)

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos" 

    def __str__(self):
        return self.anio

class Cronograma(models.Model):
    # atributos de la clase Cronograma

   periodo = models.OneToOneField(Periodo, on_delete=models.CASCADE)
   nombre_cronograma = models.CharField(verbose_name="Cronograma", max_length=50)
   empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE )
   actividad = models.CharField(verbose_name="Actividad", max_length=100, null = False)
   observaciones = models.TextField(verbose_name="Observaciones", null = True, blank= True)
   responsable = models.CharField(verbose_name="Responsable", max_length=250, null = False)
   valor_presupuestado= models.DecimalField(verbose_name="Valor Presupuestado", max_digits= 15, decimal_places= 2)
   create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
   modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

   class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronogramas" 

   def __str__(self):
        return self.nombre_cronograma

class Ejecucion(models.Model):

    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", null=True)
    numero_factura = models.CharField(verbose_name="Número de factura", max_length=20, null = False)
    actividad = models.CharField(verbose_name="Actividad", max_length=250, null = False)
    cantidad = models.CharField(verbose_name="cantidad", max_length=250, null = False)
    valor_unitario = models.DecimalField(verbose_name="Valor Unitario", max_digits= 15, decimal_places= 2)
    valor_iva = models.DecimalField(verbose_name="Valor IVA", max_digits= 15, decimal_places= 2)
    total_unidades = models.DecimalField(verbose_name="Total Unidades", max_digits= 15, decimal_places= 2)
    total_ejecucion = models.DecimalField(verbose_name="Total Ejecución", max_digits= 15, decimal_places= 2)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Ejecucion"
        
    def __str__(self):
        return self.total_ejecucion
