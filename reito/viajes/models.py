from django.db import models
from datetime import date

from django.db.models.fields import CharField, DecimalField, IntegerField

# Create your models here.

class Destino(models.Model):
    nombre = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return self.nombre

class Viaje(models.Model):
    destino = models.ForeignKey("viajes.Destino", verbose_name='Destino', on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", default=date.today)
    asientos = IntegerField('Asientos')
    precio = DecimalField('Precio', max_digits=5, decimal_places=2)
    descripcion = CharField('Descripción', max_length=500)

    def __str__(self):
        return self.destino
