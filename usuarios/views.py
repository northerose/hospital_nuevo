from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import Persona
from .forms import RegistroForm


def usuario(request):
    return render(request, 'usuario/usuario.html')


def registro(request):

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['dni']
            user.save()

            Persona.objects.create(user=user, dni=form.cleaned_data['dni'])

            login(request, user)
            return redirect('inicio')

    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', { 'form': form})