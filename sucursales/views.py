from django.shortcuts import render

# Create your views here.

def sucursales(request):
    return render(request, 'sucursales/sucursales.html')