from django.db import models

class Usuario(models.Model): 
    login = models.CharField(
        unique=True,
        max_length=16,
    )
    senha = models.CharField(
        max_length=100
    )

class Pessoa(models.Model):
    nome = models.CharField(
        max_length=25,
    )

    idade = models.IntegerField()

    cpf = models.CharField(
        max_length=11
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT
    )


