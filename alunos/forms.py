from django import forms
from .models import *

class formulario(forms.ModelForm):

    class Meta:
        model = dados2
        fields = ('nome', 'endereço', 'email', 'curso', 'cidade')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereço': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
        }