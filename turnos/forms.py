from django import forms
from django.forms import ValidationError

from profesionales.models import Profesional
from turnos.models import Turno
from usuarios.models import Persona

class Paso1Form(forms.Form):
    sucursal = forms.IntegerField()


class Paso2Form(forms.Form):
    especialidad = forms.IntegerField()


class Paso3Form(forms.Form):
    profesional = forms.IntegerField()


class Paso4Form(forms.Form):
    profesional = forms.IntegerField()
    fecha = forms.DateField()
    hora = forms.TimeField()

    def clean(self):
        profesional = Profesional.objects.get(id=self.cleaned_data['profesional'])

        if not self.cleaned_data.get('fecha'):
            raise ValidationError('La fecha es requerida')

        if not self.cleaned_data.get('hora'):
            raise ValidationError('La hora es requerida')

        fecha = self.cleaned_data['fecha']
        hora = self.cleaned_data['hora']

        if Turno.objects.filter(profesional=profesional, fecha=fecha, hora=hora).exists():
            raise ValidationError("Este horario no esta disponible. Selecciona otro")
        return self.cleaned_data



class Paso5Form(forms.ModelForm):
    fecha = forms.DateField()
    hora = forms.TimeField()

    class Meta:
        model = Turno
        fields = ['profesional', 'persona', 'fecha', 'hora']