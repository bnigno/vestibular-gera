from django.db import models

class Distribudora(models.Model):
    nome = models.CharField(max_length=100)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()
    distribuidora = models.ForeignKey(Distribudora, on_delete=models.CASCADE)

class Fatura(models.Model):
    referencia = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)