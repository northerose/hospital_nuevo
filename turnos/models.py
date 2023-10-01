from django.db import models
from profesionales.models import Horario
from usuarios.models import Persona
# Create your models here.





class Turno(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()