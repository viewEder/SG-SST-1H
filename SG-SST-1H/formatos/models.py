from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from empresa.models import Empleados

# Create your models here.
# Modelo Quejas de acoso laboral
class QuejasAcosoLaboral(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE)
    fecha_diligenciamiento = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
