from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="nombre")
    apellido = models.CharField(max_length=30, verbose_name="apellido")
    email = models.EmailField(max_length=150, verbose_name="email") 
    dni = models.PositiveIntegerField(verbose_name="dni", unique=True)

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El Dni debe ser un numero positivo de 8 digitos")
        return self.cleaned_data['dni']

        class Meta:
          abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return self.nombre_completo()
