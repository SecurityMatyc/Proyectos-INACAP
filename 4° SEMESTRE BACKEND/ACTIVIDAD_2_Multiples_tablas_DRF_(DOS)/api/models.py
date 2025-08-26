from django.db import models
from django.contrib.auth.models import User


class Proyecto(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la Tarea")
    completada = models.BooleanField(
        default=False, verbose_name="¿Completada?")
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, verbose_name="Proyecto")

    def __str__(self):
        return self.nombre
