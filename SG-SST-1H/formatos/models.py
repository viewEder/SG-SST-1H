from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from empresa.models import Empleados

# Create your models here.
# crear una función que permita adjuntar documentos
def adjuntos_quejas(instance, filename):
    old_instance = QuejasAcosoLaboral.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docsquejas/' + filename

# Modelo Quejas de acoso laboral
class QuejasAcosoLaboral(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE)
    fecha_diligenciamiento = models.DateField(auto_now_add=True, verbose_name="Fecha")
    hechos = models.TextField(verbose_name="Descripción de los hechos",null=False)
    pruebas = models.TextField(verbose_name="Descripción de pruebas",null=False)
    adjuntos = models.FileField(upload_to=adjuntos_quejas,null= True, blank= True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Queja de acoso laboral"
        verbose_name_plural = "Quejas de acoso laboral"
        
    def __str__(self) -> str:
        return self.nombre_documento