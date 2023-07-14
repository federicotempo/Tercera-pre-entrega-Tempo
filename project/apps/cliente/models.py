from django.db import models

# Create your models here.


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sexo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    documento = models.IntegerField()
    provincia_id = models.ForeignKey(
        Provincia, on_delete=models.SET_NULL, null=True, blank=True)
    sexo_id = models.ForeignKey(
        Sexo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
