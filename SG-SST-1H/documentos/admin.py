from django.contrib import admin
from .models import *

# class para visualizar tipo de empresa
class TipoDocumentoAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('nombre_tipo', )
    ordering = ('nombre_tipo', )
    list_filter = ('nombre_tipo', )
    search_fields = ('nombre_tipo', )

class Meta:
    model = (TipoDocumento)

admin.site.register (TipoDocumento, TipoDocumentoAdmin)

class DocuEmpresaAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('empresa','nombre_documento',)
    ordering = ('empresa', 'nombre_documento')
    list_filter = ('empresa', )
    search_fields = ('empresa',)
class Meta:
    model = (DocuEmpresa)

admin.site.register (DocuEmpresa, DocuEmpresaAdmin)
# Register your models here.

class DocuEmpleadosAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('empleado','tipo_documento','nombre_documento')
    ordering = ('empleado', 'nombre_documento',)
    list_filter = ('empleado', )
    search_fields = ('empleado', )

class Meta:
    model = (DocuEmpleados)

admin.site.register (DocuEmpleados, DocuEmpleadosAdmin)

class DocsComiteAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('comite','tipo_documento','nombre_documento')
    ordering = ('comite', 'nombre_documento',)
    list_filter = ('comite', )
    search_fields = ('comite', )

class Meta:
    model = (DocsComite)

admin.site.register (DocsComite, DocsComiteAdmin)