from django.db import models
from usuarios.models import Persona
from sucursales.models import Sucursal

# Create your models here.


class Especialidad(models.Model):
    nombre = models.CharField(max_length=200)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    


class Profesional(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=8)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.persona.nombre


class Horario(models.Model):
    horarios = [
        ('manana', "Mañana"),
        ('tarde', "Tarde"),
        ('noche', "Noche"),
    ]

    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100, choices= horarios, default='manana')

