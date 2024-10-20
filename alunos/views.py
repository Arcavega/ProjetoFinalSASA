from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, 'index.html')