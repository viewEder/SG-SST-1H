from django.db import models
from django.db.models.deletion import CASCADE
from empresa.models import Empresa, Empleados
from comites.models import Comites

# funcion para subir documentos

def subir_documentos(instance, filename):
    old_instance = DocuEmpresa.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docsempresa/' + filename

def subir_docuEmpleados(instance, filename):
    old_instance = DocuEmpleados.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docsempleados/' + filename

def subir_docscomite(instance, filename):
    old_instance = DocsComite.objects.get(pk=instance.pk)
    old_instance.path_documento.delete()
    return 'recursos/docscomite/' + filename


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
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=CASCADE, default=1)
    nombre_documento = models.CharField(verbose_name = "nombre del documento", max_length = 50, null = False)
    path_documento = models.FileField(verbose_name="Archivo", upload_to= subir_documentos, null= True, blank= True)
    subido_el = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Subido el")
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")

    
    class Meta:
        verbose_name = "Documento Empresa"
        verbose_name_plural = "Documentos Empresas"
        
    def __str__(self) -> str:
        return self.nombre_documento

class DocuEmpleados(models.Model):
    # atributo de la clase ducumento empresa
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=CASCADE, default=1)
    nombre_documento = models.CharField(verbose_name = "nombre del documento", max_length = 50, null = False)
    path_documento = models.FileField(verbose_name="Archivo", upload_to= subir_docuEmpleados, null= True, blank= True)
    subido_el = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Subido el")
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")

    
    class Meta:
        verbose_name = "Documento empleado"
        verbose_name_plural = "Documentos empleados"
        
    def __str__(self) -> str:
        return self.nombre_documento

class DocsComite(models.Model):
    # atributo de la clase ducumento comite
    comite = models.ForeignKey(Comites, on_delete=CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=CASCADE, default=1)
    nombre_documento = models.CharField(verbose_name = "nombre del documento", max_length = 50, null = False)
    path_documento = models.FileField(verbose_name="Archivo", upload_to= subir_docscomite, null= True, blank= True)
    subido_el = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Subido el")
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Creado el") 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Actualizado el")

    
    class Meta:
        verbose_name = "Documento comite"
        verbose_name_plural = "Documentos comites"
        
    def __str__(self) -> str:
        return self.nombre_documento