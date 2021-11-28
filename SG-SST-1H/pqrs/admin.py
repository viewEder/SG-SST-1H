from django.contrib import admin
from .models import *

# Register your models here.
class QuejasAdmin(admin.ModelAdmin):
    readonly_fields =('create_at', 'modify_at', 'queja', 'usuario', 'evidencia')
    list_display = ('queja','evidencia')
    ordering = ('create_at', 'queja',)
    list_filter = ('usuario__username', )
    search_fields = ('usuario__username', 'queja')
    
admin.site.register(Quejas, QuejasAdmin)

class AccionesAdmin(admin.ModelAdmin):
    readonly_fields =('create_at', 'modify_at')
    list_display = ('queja','nota_accion', 'estado')
    ordering = ('create_at', 'nota_accion',)
    list_filter = ('estado','queja__usuario')
    search_fields = ('queja__usuario', 'queja', 'nota_accion', 'estado')
    
admin.site.register(AccionesQueja, AccionesAdmin)