from django.db import models
from django import forms

# Create your models here.

class Servicos (models.Model):
    nome = models.CharField(max_length=100)

class FormServicos (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.IntegerField()
    mensagem = models.TextField()
    servico = models.ForeignKey(Servicos, on_delete= models.CASCADE)