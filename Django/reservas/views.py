# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, viewsets
from reservas.models import *
from reservas.serializers import *
from django.shortcuts import render

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new post."""
        serializer.save()

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ParqueaderoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer