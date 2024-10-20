from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    formularios = FormServicos.objects.all()
    return render(request, 'index.html', context = {'formularios': formularios})

def cadastrar(request):
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dados')
    else:

        form = formulario()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
    

