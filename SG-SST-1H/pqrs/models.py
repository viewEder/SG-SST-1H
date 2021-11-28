from django.db import models
from django.contrib.auth.models import User
from core.types.sino import SiNo
from core.types.estadospqrs import EstadoAtencion
from django.db.models.deletion import CASCADE

def subir_evidencia(instance, filename):
    return "recursos/pqrs/" + filename

# Create your models here.
class Quejas(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    queja = models.TextField(verbose_name="Queja", null = False)
    evidencia = models.CharField(verbose_name="¿Cuenta con evidencia?", choices=SiNo, max_length=2, default="No")
    soporte = models.FileField(upload_to=subir_evidencia, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Registrado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "PQRS Acoso laboral"
        verbose_name_plural = "PQRS Acoso laboral"
    
    def __str__(self) -> str:
        return f'{self.queja[0:15]} Ver más'

class AccionesQueja(models.Model):
    queja = models.ForeignKey(Quejas, on_delete=CASCADE)
    nota_accion = models.TextField(verbose_name="Acciones sobre la queja", null = False)
    estado = models.CharField(verbose_name="Estado de la Acción", max_length=25, choices=EstadoAtencion, null=False, default="Sin Atender")
    create_at = models.DateField(auto_now_add=True, verbose_name="Registrado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Atenciones"
        verbose_name_plural = "Atenciones"
    
    def __str__(self) -> str:
        return f'{self.nota_accion[0:15]} Ver más'