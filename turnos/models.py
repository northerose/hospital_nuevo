from django.db import models
from profesionales.models import Profesional
from usuarios.models import Persona

# Create your models here.

class Turno(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()
    