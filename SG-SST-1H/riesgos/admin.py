from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register (Evaluacion)
admin.site.register (TipoRiesgo)
admin.site.register (AmenazaRiesgo)
admin.site.register (ClasificacionesRiesgos)
admin.site.register (CausaAmenaza)
admin.site.register (OrigenAmenaza)
admin.site.register (DetalleAmenaza)
