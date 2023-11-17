from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from .models import Persona


class RegistroForm(UserCreationForm):
    dni = forms.IntegerField(min_value=100000, max_value=99999999)

    class Meta:
        model = User
        fields = ['dni', 'first_name', 'last_name', 'email','password1','password2']

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni:
            raise ValidationError('El campo DNI es requerido')

        if Persona.objects.filter(dni=dni).exists():
            raise ValidationError('Ya existe un paciente registrado con este DNI')


        if User.objects.filter(username=dni).exists():
            raise ValidationError('Ya existe un usuario registrado con este DNI')

        return dni

