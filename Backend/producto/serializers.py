from rest_framework import serializers
from producto import models

class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Producto
    fields = '__all__'