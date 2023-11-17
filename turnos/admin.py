from django.contrib import admin
from .models import Turno

# Register your models here.

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['profesional', 'persona', 'fecha', 'hora']
