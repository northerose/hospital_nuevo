from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from .forms import ContactoForm
from django.contrib import messages
from .models import Noticia

# Create your views here.

def inicio(request):
    titulo = 'inicio'
    noticias = Noticia.objects.all() 
    return render(request, 'inicio/inicio.html', {'titulo': titulo, 'noticias': noticias})

def contacto(request):

    if request.method == 'GET':
        formulario = ContactoForm()
    elif request.method == 'POST':
        formulario = ContactoForm(request.POST)
        # # Acá hago todo lo que impacta en el sistema (envio de email, grabar datos, etc)
        if formulario.is_valid():
            messages.success(request, 'Hemos recibido tus datos')
            return redirect(reverse ('inicio'))
        else:
            messages.error(
                request, 'Por favor revisa los errores en el formulario')
    else:
        return HttpResponseBadRequest("Mandaste cualquiera IMBECIL")

    context={
        'contacto_form': formulario
        
    }
    return render(request, 'inicio/contacto.html', context)



