from django.contrib import admin
from .models import Sucursal

# Register your models here.

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    pass