from restfulapi.quickstart import models
from rest_framework import serializers


class DistribuidoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Distribudora
        fields = ['nome']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ['nome', 'numero', 'distribuidora']

class FaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fatura
        fields = ['referencia', 'valor', 'cliente']