from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
 
# Create your models here.

# Modelo tipo de empresa
class TipoEmpresa(models.Model):
    # atributo de la clase tipo de empresa
    nombre_tipo = models.CharField(verbose_name = "Tipo de empresa", max_length = 150, null = False)
    
    class Meta:
        verbose_name = "Tipo de empresa"
        verbose_name_plural = "Tipo de empresas"
    
# Modelo empresa 
class Empresa (models.Model):
    # atributos de la clase empresa
    tipo_empresa = models.OneToOneField(TipoEmpresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 256, verbose_name = "Nombre de la empresa", null = False)
    nit = models.CharField(max_length = 25, verbose_name = "Número de identificación tributaria", null = False)
    actividad_economica = models.CharField(max_length = 50, verbose_name = "Actividad económica", null = False)
    nivel_de_riesgo = models.CharField(max_length = 10, verbose_name = "Nivel de riesgo", null = False)
    naturaleza_juridica = models.CharField(max_length = 50, verbose_name = "Naturaleza jurídica", null = False)
    correo_electronico = models.CharField(max_length = 25, verbose_name = "Correo electrónico", null = False)
    tipo_de_empresa = models.CharField(max_length = 25, verbose_name = "Tipo de empresa", null = False)
    numeros_telefonicos = models.CharField(max_length = 40, verbose_name = "Números telefónicos", null = False)
    
    class Meta:
        verbose_name = "Empresa"

# Modelo Areas
class Areas (models.Model):
    # atributo de la clase área
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_area = models.CharField(max_length = 150, verbose_name = "Números telefónicos", null = False)
    
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        
# Modelo Empleados
class Empleados (models.Model):
    # atributos de la clase empleado
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.OneToOneField(Areas, on_delete=models.CASCADE)
    id_empleado = models.CharField(max_length = 30, verbose_name = "ID empleado", null = True)
    fecha_ingreso = models.DateField(verbose_name = "Fecha de ingreso", auto_now = False, auto_now_add = False)
    cargo = models.CharField(max_length = 30, verbose_name = "Cargo del empleado", null = False)
    sueldo = models.DecimalField(verbose_name = "Sueldo", max_digits = 12, decimal_places = 2)
    nivel = models.CharField(max_length = 40, verbose_name = "Nivel", null = False)
    eps = models.CharField(max_length = 100, verbose_name = "EPS", null = False)
    arl = models.CharField(max_length = 100, verbose_name = "ARL", null = False)
    cuenta_bancaria = models.CharField(max_length = 30, verbose_name = "Número de cuenta bancaria",null = True )
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"