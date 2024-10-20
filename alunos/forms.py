from django import forms
from .models import *

class formulario(forms.ModelForm):

    class Meta:
        model = FormServicos
        fields = "__all__"

        #widgets = {
            #'nome': forms.TextInput(attrs={'class': 'form-control'}),
            #'endereço': forms.TextInput(attrs={'class': 'form-control'}),
            #'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            #'email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'curso': forms.TextInput(attrs={'class': 'form-control'}),
        #}