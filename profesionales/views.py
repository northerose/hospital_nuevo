from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login(request):
    return render(request,('profesionales/profesionales.html'))