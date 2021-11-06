from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import Areas

# Create your models here.
class Evaluacion(models.Model):
    # atributo de la clase Evaluación
    fecha_evaluacion= models.DateField(auto_now=False, verbose_name="Fecha de la Evaluación")
    nombre_evaluacion= models.CharField(verbose_name = "Nombre de la evaluación", max_length = 350, null = False)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Nombre de la evaluación"
        verbose_name_plural = "Nombre de las evaluaciones"
            
    def __str__(self) -> str:
        return self.nombre_evaluacion

class TipoRiesgo(models.Model):
    # atributo de la clase tipo de riesgo
    tipo_riesgo= models.CharField(verbose_name = "Tipo de riesgo", max_length = 350, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Tipo de riesgo"
        verbose_name_plural = "Tipos de riesgos"
        
    def __str__(self) -> str:
        return self.tipo_riesgo

class AmenazaRiesgo(models.Model):
    # atributo de la clase amenaza riesgo
    tipo_riesgo = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)
    nombre_amenaza= models.CharField(verbose_name = "Nombre de la amenaza", max_length = 350, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Nombre de la amenaza"
        verbose_name_plural = "Nombre de las amenazas"
        
    def __str__(self) -> str:
        return self.nombre_amenaza

class ClasificacionesRiesgos(models.Model):
    # atributo de la clase clasificaciones de los riesgos
    amenaza_riesgo = models.ForeignKey(AmenazaRiesgo, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    clasificaciones_riesgos= models.CharField(verbose_name = "clasificaciones de los riesgos", max_length = 350, null = False)
    resultados= models.CharField(verbose_name = "resultado", max_length = 50, null = False)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "clasificacion del riesgo"
        verbose_name_plural = "clasificaciones de los riesgos"
            
    def __str__(self) -> str:
        return self.clasificaciones_riesgos

class CausaAmenaza(models.Model):
    # atributo de la clase Causa amenaza
    amenaza_riesgo = models.ForeignKey(AmenazaRiesgo, on_delete=models.CASCADE)
    nombre_causa_amenaza= models.CharField(verbose_name = "Nombre de la causa de la amenaza", max_length = 350, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Nombre de la causa de la amenaza"
        verbose_name_plural = "Nombre de la causas de las amenazas"
        
    def __str__(self) -> str:
        return self.nombre_causa_amenaza

class OrigenAmenaza(models.Model):
    # atributo de la clase origen amenaza
    nombre_origen_amenaza= models.CharField(verbose_name = "Nombre del origen de la amenaza", max_length = 350, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Nombre del origen de la amenaza"
        verbose_name_plural = "Nombre del origen de las amenazas"
        
    def __str__(self) -> str:
        return self.nombre_origen_amenaza

class DetalleAmenaza(models.Model):
    # atributo de la clase Detalle amenaza
    areas= models.ForeignKey(Areas, on_delete=CASCADE)
    origen_amenaza = models.ForeignKey(OrigenAmenaza, on_delete=models.CASCADE)
    causa_amenaza = models.ForeignKey(CausaAmenaza, on_delete=models.CASCADE)
    detalles_amenaza= models.CharField(verbose_name = "Detalle de la amenaza", max_length = 350, null = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Detalle de la amenaza"
        verbose_name_plural = "Detalle de las amenazas"
        
    def __str__(self) -> str:
        return self.detalles_amenaza