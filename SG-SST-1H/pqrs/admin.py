from django.contrib import admin
from .models import *

# Register your models here.
class QuejasAdmin(admin.ModelAdmin):
    readonly_fields =('create_at', 'modify_at')
    list_display = ('queja','evidencia')
    ordering = ('create_at', 'queja',)
    list_filter = ('usuario__username', )
    search_fields = ('usuario__username', 'queja')
    
admin.site.register(Quejas, QuejasAdmin)

class AccionesAdmin(admin.ModelAdmin):
    readonly_fields =('_create_at', '_modify_at')
    list_display = ('queja','_nota_accion', '_estado')
    ordering = ('_create_at', '_nota_accion',)
    list_filter = ('_estado','queja__usuario')
    search_fields = ('queja__usuario', 'queja', '_nota_accion', '_estado')
    
admin.site.register(AccionesQueja, AccionesAdmin)