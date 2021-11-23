from django.contrib import admin
from .models import *

# Register your models here.
class PlanAnualAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')  # no permite modificar estos campos
    list_display = ('anio', 'metas',)
    ordering = ('anio',)
    list_filter = ('anio',)
    search_fields = ('anio', 'metas',)
    
    
admin.site.register(PlanAnual, PlanAnualAdmin)

class EstructuraSGSSTAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')  # no permite modificar estos campos
    list_display = ('nombre', 'abreviatura',)
    ordering = ('nombre',)
    list_filter = ('nombre', 'abreviatura',)
    search_fields = ('nombre', 'abreviatura',)
    
admin.site.register(EstructuraSGSST, EstructuraSGSSTAdmin)

class ActividadesPlanAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')  # no permite modificar estos campos
    list_display = ('id_responsable', 'actividad', 'fecha_planeacion')
    ordering = ('actividad',)
    list_filter = ('actividad', 'id_responsable', )
    search_fields = ('actividad', 'id_responsable',)
    
admin.site.register(ActividadesPlan, ActividadesPlanAdmin)

class CumplimientoActividadesAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')  # no permite modificar estos campos
    list_display = ('fecha_cumplimiento', 'id_actividad',)
    ordering = ('id_actividad',)
    list_filter = ('fecha_cumplimiento', 'id_actividad',)
    search_fields = ('id_actividad',)
    
admin.site.register(CumplimientoActividades, CumplimientoActividadesAdmin)
