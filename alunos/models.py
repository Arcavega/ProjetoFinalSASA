from django.db import models
from django import forms

# Create your models here.



class dados2(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    endereço = models.CharField(max_length=200)
    cidade = models.CharField(max_length=300)
    curso = models.CharField(max_length=300)
    img = models.ImageField(upload_to="./Imagens/", null=True)
    

    def __str___(self):
        return self.nome



