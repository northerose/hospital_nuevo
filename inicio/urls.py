from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('noticias/<int:noticia_id>/', views.noticias, name='noticias'),
]