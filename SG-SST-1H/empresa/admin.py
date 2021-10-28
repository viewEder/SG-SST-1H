from django.contrib import admin
from .models import TipoEmpresa, Empresa, Areas, Empleados

# Register your models here.
admin.site.register(TipoEmpresa)
admin.site.register(Areas)
admin.site.register(Empleados)
admin.site.register(Empresa)
