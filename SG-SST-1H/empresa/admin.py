from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TipoEmpresa)
admin.site.register(Areas)
admin.site.register(Empleados)
admin.site.register(Empresa)
admin.site.register(Cargos)
admin.site.register(NivelAcademico)

