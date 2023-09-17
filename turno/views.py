from django.shortcuts import render

# Create your views here.

def turno(request):
    return render(request, 'turno/turno.html')