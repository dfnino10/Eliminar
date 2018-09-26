from rest_framework import serializers
from . import models


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'usuario', 'parqueadero', 'fecha')
        model = models.Reserva

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombres', 'apellidos', 'nombreusuario')
        model = models.Usuario

class ParqueaderoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'direccion', 'cupos')
        model = models.Parqueadero