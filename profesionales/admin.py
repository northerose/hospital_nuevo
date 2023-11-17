from django.contrib import admin
from .models import Profesional, Horario, Especialidad

# Register your models here.

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['persona', 'matricula', 'especialidad']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['profesional', 'horario']


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'sucursal']