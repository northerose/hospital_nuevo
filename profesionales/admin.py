from django.contrib import admin
from .models import Profesional, Horario, Especialidad

# Register your models here.

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    pass


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    pass