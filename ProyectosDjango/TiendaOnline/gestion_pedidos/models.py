from django.db import models
from django.forms.models import model_to_dict

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

    def __str__(self):
        # return str(self.__class__.__name__) + ': ' + str(self.__dict__)
        return str(self.__class__.__name__) + ': ' + str(model_to_dict(self))


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    # def __str__(self):
    #     # return str(self.__class__.__name__) + ': ' + str(self.__dict__)
    #     return str(self.__class__.__name__) + ': ' + str(model_to_dict(self))


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        # return str(self.__class__.__name__) + ': ' + str(self.__dict__)
        return str(self.__class__.__name__) + ': ' + str(model_to_dict(self))
