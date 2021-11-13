from django.contrib import admin
from .models import *


# Register your models here.
class EvaluacionAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('fecha_evaluacion','nombre_evaluacion')
    ordering = ('fecha_evaluacion', 'nombre_evaluacion',)
    list_filter = ('nombre_evaluacion', )
    search_fields = ('nombre_evaluacion', )

class Meta:
    model = (Evaluacion)

admin.site.register (Evaluacion, EvaluacionAdmin)

class TipoRiesgoAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('tipo_riesgo',)
    ordering = ('tipo_riesgo',)
    list_filter = ('tipo_riesgo', )
    search_fields = ('tipo_riesgo', )

class Meta:
    model = (TipoRiesgo)

admin.site.register (TipoRiesgo, TipoRiesgoAdmin)

class AmenazaRiesgoAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('tipo_riesgo','nombre_amenaza')
    ordering = ('tipo_riesgo', 'nombre_amenaza')
    list_filter = ('nombre_amenaza', )
    search_fields = ('nombre_amenaza', )

class Meta:
    model = (AmenazaRiesgo)

admin.site.register (AmenazaRiesgo, AmenazaRiesgoAdmin)

class ClasificacionesRiesgosAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('amenaza_riesgo','evaluacion', 'clasificaciones_riesgos', 'resultados')
    ordering = ('amenaza_riesgo','evaluacion', 'clasificaciones_riesgos')
    list_filter = ('clasificaciones_riesgos', )
    search_fields = ('clasificaciones_riesgos', )

class Meta:
    model = (ClasificacionesRiesgos)

admin.site.register (ClasificacionesRiesgos, ClasificacionesRiesgosAdmin)

class CausaAmenazaAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('amenaza_riesgo','nombre_causa_amenaza')
    ordering = ('amenaza_riesgo','nombre_causa_amenaza')
    list_filter = ('nombre_causa_amenaza', )
    search_fields = ('nombre_causa_amenaza', )

class Meta:
    model = (CausaAmenaza)

admin.site.register (CausaAmenaza, CausaAmenazaAdmin)

class OrigenAmenazaAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('nombre_origen_amenaza',)
    ordering = ('nombre_origen_amenaza',)
    list_filter = ('nombre_origen_amenaza', )
    search_fields = ('nombre_origen_amenaza', )

class Meta:
    model = (OrigenAmenaza)

admin.site.register (OrigenAmenaza, OrigenAmenazaAdmin)

class DetalleAmenazaAdmin(admin.ModelAdmin):
    reandoly_fields =('create_at', 'modify_at')
    list_display = ('areas','origen_amenaza', 'causa_amenaza','detalles_amenaza')
    ordering = ('areas','origen_amenaza', 'causa_amenaza','detalles_amenaza')
    list_filter = ('detalles_amenaza', )
    search_fields = ('detalles_amenaza', )

class Meta:
    model = (DetalleAmenaza)

admin.site.register (DetalleAmenaza, DetalleAmenazaAdmin)
