from django.shortcuts import render

# Create your views here.

def inicio(request):
    titulo = 'inicio'
    return render(request, 'inicio/inicio.html', {'titulo': titulo})

