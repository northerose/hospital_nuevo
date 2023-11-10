from django import forms
import re
from django.forms import ValidationError



def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s', code='Invalid', params={'valor': value})


def custom_validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, validators=(solo_caracteres,), widget=forms.TextInput( attrs={'class': 'form-control','placeholder': 'Nombre (Solo letras)'}))
    apellido = forms.CharField(label='Apellido', max_length=50, validators=(solo_caracteres,), widget=forms.TextInput( attrs={'class': 'form-control','placeholder': 'Apellido (Solo letras)'}))
    email = forms.EmailField(label='Email', max_length=100, required=True, error_messages={'required': 'Por favor completa el campo'}, widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'example@example.com'}))
    asunto = forms.CharField(label='Asunto', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Asunto'}))
    mensaje = forms.CharField(label='Mensaje', max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'class':'form-control'}))

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError(
                "Debes especificar mejor el mensaje que nos envias")
        return data
    
    










    


#     def clean(self):
#         cleaned_data = super().clean()
#         nombre = cleaned_data.get("nombre")
#         suscripcion = cleaned_data.get("suscripcion")

#         if suscripcion and nombre and ("HOMERO" in nombre.upper()):
#             msg = "No le brindamos información a Homeros."
#             self.add_error('nombre', msg)
#             raise ValidationError(msg)