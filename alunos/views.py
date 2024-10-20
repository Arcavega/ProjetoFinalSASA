from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    formularios = FormServicos.objects.all()
    context = {'formularios': formularios}
    return render(request, 'index.html', context)

def cadastrar(request):
    cadastro = formulario()
    context = {'form': form}
    return render(request, 'index.html', context)