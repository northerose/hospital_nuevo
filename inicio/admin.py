from django.contrib import admin
from .models import Noticia, Recomendacion, ObraSocial, Etiquetas

# Register your models here.

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'fuente']


@admin.register(Recomendacion)
class RecomendacionAdmin(admin.ModelAdmin):
    pass

@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    pass


@admin.register(Etiquetas)
class EtiquetasAdmin(admin.ModelAdmin):
    list_display = ['nombre']