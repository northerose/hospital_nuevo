from django.urls import path
from . import views

urlpatterns = [
                path('', views.turno, name='turno')
]