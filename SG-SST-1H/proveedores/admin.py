from django.contrib import admin
from .models import *

# Register your models here.

class ProveedoresAdmin(admin.ModelAdmin):
    readondly_fields = ('create_at, modify_at',)
    list_display = ('nombre_empresa', 'nit', 'id_proveedor', 'certificado_arl', ) 
    ordering = ('tipo_empresa', 'nombre_empresa',)
    list_filter = ('nombre_empresa',)
    search_field = ('nombre_empresa',)
    

admin.site.register(Proveedores, ProveedoresAdmin)

class ElementosAdmin(admin.ModelAdmin):
    readondly_fields = ('create_at, modify_at',)
    list_display = ('nombre_elemento', 'fecha_creacion', 'activo',)
    ordering = ('id_elemento', 'nombre_elemento',)
    list_filter = ('nombre_elemento',)
    search_field = ('nombre_elemento',)
    

admin.site.register(Elementos, ElementosAdmin)


class DetalleElementosAdmin(admin.ModelAdmin):
    readondly_fields = ('create_at, modify_at',)
    list_display = ('id_elemento', 'descripcion', 'vida_util', 'activo', 'fecha_creacion',)
    ordering = ('id_proveedor', 'id_elemento',)
    list_filter = ('id_elemento',)
    search_field = ('id_elemento',)


admin.site.register(DetalleElementos, DetalleElementosAdmin)

