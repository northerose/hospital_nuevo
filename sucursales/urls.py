from django.urls import path
from . import views

urlpatterns = [
                path('', views.sucursales, name='sucursales'),
]