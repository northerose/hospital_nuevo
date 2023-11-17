from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.usuario, name='usuario'),
    path('registro', views.registro, name='registro'),
]