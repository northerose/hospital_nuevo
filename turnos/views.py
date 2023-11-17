from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from sucursales.models import Sucursal
from profesionales.models import Especialidad, Profesional, Horario

from .forms import Paso1Form, Paso2Form, Paso3Form, Paso4Form, Paso5Form
from .models import Turno



@login_required
def turno_p1(request):
    if request.method == "POST":
        form = Paso1Form(request.POST)
        if form.is_valid():
            sucursal = form.cleaned_data['sucursal']
            # reverse('turno_p2', args=[sucursal]) es lo mismo que '/turnos/crear/paso2/1'
            return HttpResponseRedirect(reverse('turno_p2', args=[sucursal]))
    else:
        form = Paso1Form()

    sucursales = Sucursal.objects.all()

    return render(request, 'turno/turno_p1.html', {'form': form, 'sucursales': sucursales})


@login_required
def turno_p2(request, sucursal_id):
    if request.method == "POST":
        form = Paso2Form(request.POST)
        if form.is_valid():
            especialidad = form.cleaned_data['especialidad']
            return HttpResponseRedirect(reverse('turno_p3', args=[especialidad]))
    else:
        form = Paso2Form()

    especialidades = Especialidad.objects.filter(sucursal_id=sucursal_id)

    return render(request, 'turno/turno_p2.html', {'form': form, 'especialidades': especialidades})


@login_required
def turno_p3(request, especialidad_id):
    if request.method == "POST":
        form = Paso3Form(request.POST)
        if form.is_valid():
            profesional = form.cleaned_data['profesional']
            return HttpResponseRedirect(reverse('turno_p4', args=[profesional]))
    else:
        form = Paso3Form()

    profesionales = Profesional.objects.filter(especialidad_id=especialidad_id)

    return render(request, 'turno/turno_p3.html', {'form': form, 'profesionales': profesionales})


@login_required
def turno_p4(request, profesional_id):
    if request.method == "POST":
        datos = {
            'profesional': profesional_id,
            'fecha': request.POST.get('fecha'),
            'hora': request.POST.get('hora'),
        }
        form = Paso4Form(datos)
        if form.is_valid():
            profesional = profesional_id
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            return HttpResponseRedirect(reverse('turno_p5') + f'?profesional={profesional}&fecha={fecha}&hora={hora}')
    else:
        form = Paso4Form()


    hora_minimo = None
    hora_maximo = None

    for horario in Horario.objects.filter(profesional_id=profesional_id):
        if horario.horario == 'manana':
            hora_minimo = 7
            hora_maximo = 12
        elif horario.horario == 'tarde':
            if not hora_minimo:
                hora_minimo = 12
            hora_maximo = 18
        elif horario.horario == 'noche':
            if not hora_minimo:
                hora_minimo = 18
            hora_maximo = 21

    horarios = []
    for hora in range(hora_minimo, hora_maximo):
        horarios.append(f'{hora}:00')

    return render(request, 'turno/turno_p4.html', {'form': form, 'horarios': horarios})


@login_required
def turno_p5(request):
    if request.method == "POST":
        datos = {
            'persona': request.user.persona,
            'profesional': request.POST.get('profesional'),
            'fecha': request.POST.get('fecha'),
            'hora': request.POST.get('hora'),
        }
        form = Paso5Form(datos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('turno_p5'))
    else:
        form = Paso5Form()

    profesional = Profesional.objects.get(id=request.GET.get('profesional'))
    fecha = request.GET.get('fecha')
    hora = request.GET.get('hora')

    return render(request, 'turno/turno_p5.html', {'form': form, 'profesional': profesional, 'fecha': fecha, 'hora': hora})


@login_required
def mis_turnos(request):

    turnos = Turno.objects.filter(persona=request.user.persona)

    return render(request, 'turno/mis_turnos.html', {'turnos': turnos})
