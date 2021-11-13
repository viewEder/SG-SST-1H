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
    list_filter = ('nombre_documento', )
    search_fields = ('nombre_documento',)
class Meta:
    model = (DocuEmpresa)

admin.site.register (DocuEmpresa, DocuEmpresaAdmin)
# Register your models here.

class DocuEmpleadosAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('empresa','nombre_documento')
    ordering = ('empresa', 'nombre_documento',)
    list_filter = ('nombre_documento', )
    search_fields = ('nombre_documento', )

class Meta:
    model = (DocuEmpresa, DocuEmpleadosAdmin)


admin.site.register (DocuEmpleados)
admin.site.register (DocsComite)