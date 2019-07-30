from restfulapi.quickstart.models import Distribudora, Cliente, Fatura
from rest_framework import viewsets
from restfulapi.quickstart.serializers import DistribuidoraSerializer, ClienteSerializer, FaturaSerializer


class DistribuidoraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Distribudora.objects.all()
    serializer_class = DistribuidoraSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer