from django.db import models

class Producto(models.Model):

  nombre = models.CharField(max_length=255)
  imagen = models.TextField()
  precio = models.DecimalField(decimal_places=2, max_digits=10)
  artesano = models.CharField(max_length=255)
  sku = models.CharField(max_length=255)

  def __str__(self):
    return self.nombre