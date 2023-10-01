from django.contrib import admin
from .models import Noticia, Recomendacion, ObraSocial

# Register your models here.

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Recomendacion)
class RecomendacionAdmin(admin.ModelAdmin):
    pass

@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    pass