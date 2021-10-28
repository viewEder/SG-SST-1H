from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import Empresa, Empleados

# funcion para subir documentos

def subir_documentos(instance, filename):
    old_instance = DocuEmpresa.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docsempresa/' + filename

def subir_docuEmpleados(instance, filename):
    old_instance = DocuEmpleados.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docsempleados/' + filename

# Create your models here.

class TipoDocumento(models.Model):
    # atributo de la clase tipo de documento
    nombre_tipo = models.CharField(verbose_name = "Tipo de documento", max_length = 50, null = False)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipo de documentos"
        
    def __str__(self) -> str:
        return self.nombre_tipo

class DocuEmpresa(models.Model):
    # atributo de la clase ducumento empresa
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    nombre_documento = models.CharField(verbose_name = "nombre del documento", max_length = 50, null = False)
    path_documento = models.FileField(upload_to= subir_documentos, null= True, blank= True)
    subido_el = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Subido el")
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")

    
    class Meta:
        verbose_name = "Nombre documento"
        verbose_name_plural = "Nombre documentos"
        
    def __str__(self) -> str:
        return self.nombre_documento

class DocuEmpleados(models.Model):
    # atributo de la clase ducumento empresa
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE)
    nombre_documento = models.CharField(verbose_name = "nombre del documento", max_length = 50, null = False)
    path_documento = models.FileField(upload_to= subir_docuEmpleados, null= True, blank= True)
    subido_el = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Subido el")
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")

    
    class Meta:
        verbose_name = "Nombre documento empleado"
        verbose_name_plural = "Nombre documentos empleados"
        
    def __str__(self) -> str:
        return self.nombre_documento