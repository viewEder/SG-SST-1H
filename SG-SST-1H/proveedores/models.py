from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import TipoEmpresa
from core.types.sino import SiNo


# Create your models here.

class Proveedores(models.Model):
    # Atributo de la clase proveedores
    tipo_empresa = models.OneToOneField(TipoEmpresa, on_delete= CASCADE)
    nombre_empresa = models.CharField(max_length = 100, verbose_name = "Nombre de la empresa", null = False)
    nit = models.CharField(max_length = 25, verbose_name = "Número de identificación tributaria", null = False)
    id_proveedor = models.CharField(max_length = 30, verbose_name = "ID proveedor", null = True)
    certificado_arl = models.CharField(max_length = 50, verbose_name = "ARL", null = False)
    es_autorizado = models.CharField(verbose_name= "Se encuentra autorizado?", choices= SiNo, max_length= 2)
    seguridad_social = models.CharField(max_length = 50, verbose_name = "EPS", null = False)
    ficha_seguridad_social = models.CharField(max_length = 256, verbose_name = "Ficha seguridad social", null = False)
    telefono1 = models.CharField(max_length = 40, verbose_name = "Número telefónico 1", null = False)
    telefono2 = models.CharField(max_length = 40, verbose_name = "Número telefónico 2", null = False)
    email = models.CharField(max_length = 50, verbose_name = "Email", null = False)
    activo = models.CharField(verbose_name= "Se encuentra activo?", choices= SiNo, max_length= 2)
    fecha_creacion = models.DateField(verbose_name = "Fecha de creación", auto_now = False, auto_now_add = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        
    # Método string que devuelve los proveedores
    def __str__(self):
        return self.nombre_empresa

    
class Elementos(models.Model):
    # Atributo de la clase elementos
    id_elemento = models.CharField(max_length = 30, verbose_name = "ID elemento", null = True)
    nombre_elemento = models.CharField(max_length = 100, verbose_name = "Nombre del elemento", null = False)
    fecha_creacion = models.DateField(verbose_name = "Fecha de creación", auto_now = False, auto_now_add = False)
    activo = models.CharField(verbose_name= "Se encuentra activo?", choices= SiNo, max_length= 2)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"
        
    # Método string que devuelve los elementos
    def __str__(self):
        return self.nombre_elemento

class DetalleElementos(models.Model):
    # Atributo de la clase Detalle elementos
    id_proveedor = models.CharField(max_length = 30, verbose_name = "ID proveedor", null = True)
    id_elemento = models.CharField(max_length = 30, verbose_name = "ID elemento", null = True)
    descripcion = models.CharField(max_length = 256, verbose_name = "Descripción del elemento", null = False)
    vida_util = models.CharField(max_length = 30, verbose_name = "Vida útil", null = True)
    activo = models.BooleanField(default= False, verbose_name= "Se encuentra activo?", null= False)
    fecha_creacion = models.DateField(verbose_name = "Fecha de creación", auto_now = False, auto_now_add = False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Detalle elememto"
        verbose_name_plural = "Detalle elementos"
        
    # Método string que devuelve los detalles de los elementos
    def __str__(self):
        return self.descripcion

    

