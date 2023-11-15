from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('profesionales/', auth_views.LoginView.as_view(template_name='profesionales/profesionales.html'), name='login_profesionales'),
]