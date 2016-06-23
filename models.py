from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    boleta = models.CharField(blank=False, primary_key=True, max_length=10)
    edad = models.IntegerField(blank=True)
    foto = models.ImageField(blank=True)
