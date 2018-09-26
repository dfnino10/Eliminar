# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nombreusuario = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreusuario

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    cupos = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now())