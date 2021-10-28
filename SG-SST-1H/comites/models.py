from django.db import models

# Create your models here.
class Comites(models.Model):
    nombre_comite = models.CharField(verbose_name="Nombre de Comite", max_length=60)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Comite"
        verbose_name_plural = "Comites"
    
    def __str__(self):
        return self.nombre_comite
        
