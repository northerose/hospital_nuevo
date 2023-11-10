from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='inicio/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('noticias/<int:noticia_id>/', views.noticias, name='noticias'),
   
]