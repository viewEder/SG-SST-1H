from django.contrib import admin
from .models import *

# Register your models here.
class QuejasAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('queja','evidencia')
    ordering = ('create_at', 'queja',)
    list_filter = ('usuario__username', )
    search_fields = ('usuario__username', 'queja')
    
admin.site.register(Quejas, QuejasAdmin)

class AccionesAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('queja','nota_accion')
    ordering = ('create_at', 'nota_accion',)
    list_filter = ('queja__usuario', )
    search_fields = ('queja__usuario', 'queja', 'nota_accion')
    
admin.site.register(AccionesQueja, AccionesAdmin)