from django.shortcuts import render

# Create your views here.

def turno(request, anio):
    return render(request, 'turno/turno.html', {'anioTurno': anio})