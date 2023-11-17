from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from .forms import ContactoForm
from django.contrib import messages
from .models import Noticia, Recomendacion
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    titulo = 'inicio'
    pagina = request.GET.get('pagina')
    if pagina and pagina.isnumeric():
        pagina = int(pagina)
        siguiente_pagina = pagina + 1
        pagina_anterior = pagina-1
        noticias = Noticia.objects.all().order_by('-id')
        noticia = noticias[pagina-1]
        
    else:
        noticia = Noticia.objects.last()
        siguiente_pagina = 2
        pagina_anterior = 0
    
    total_noticias = Noticia.objects.count()

    return render(request, 'inicio/inicio.html', {'titulo': titulo, 'noticia': noticia, 'total_noticias': range(1, total_noticias+1), 'siguiente_pagina': siguiente_pagina, 'pagina_anterior': pagina_anterior})

def noticias(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render(request, 'inicio/noticias.html',  {'noticia': noticia})

def recomendaciones(request, recomendacion_id):
    recomendacion = Recomendacion.objects.get(id=recomendacion_id)
    return render(request, 'inicio/recomendaciones.html',  {'recomendacion': recomendacion})

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
        return HttpResponseBadRequest("Lo que enviaste no es correcto")

    context={
        'contacto_form': formulario
        
    }
    return render(request, 'inicio/contacto.html', context)


@login_required
def login(request):
    return redirect(reverse ('inicio'))



 






