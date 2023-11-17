from django.urls import path
from . import views

urlpatterns = [
    path('crear/paso1', views.turno_p1, name='turno_p1'),
    path('crear/paso2/<int:sucursal_id>', views.turno_p2, name='turno_p2'),
    path('crear/paso3/<int:especialidad_id>', views.turno_p3, name='turno_p3'),
    path('crear/paso4/<int:profesional_id>', views.turno_p4, name='turno_p4'),
    path('crear/paso5', views.turno_p5, name='turno_p5'),
    path('mis-turnos', views.mis_turnos, name='mis_turnos'),
]