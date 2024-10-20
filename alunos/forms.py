from django import forms
from .models import *

class formulario(forms.ModelForm):

    class Meta:
        model = FormServicos
        fields = "__all__"

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.TextInput(attrs={'class': 'form-control'}), 
        }