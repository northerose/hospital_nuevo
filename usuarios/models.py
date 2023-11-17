from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.PositiveIntegerField(verbose_name="dni", unique=True)

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El Dni debe ser un numero positivo de 8 digitos")
        return self.cleaned_data['dni']

    @property
    def nombre_completo(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def __str__(self):
        return self.nombre_completo
