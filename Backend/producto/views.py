from django.shortcuts import render
import json
import firebase_admin
from firebase_admin import db, credentials
from rest_framework.views import APIView, Response
from rest_framework import status, viewsets
from producto import serializers, models
from rest_framework.permissions import IsAuthenticated

sdk = credentials.Certificate("./Key/pruebatecnicaad-firebase-adminsdk-bs903-e9bdfd7914.json")
firebase_admin.initialize_app(sdk, {'databaseURL':"https://pruebatecnicaad-default-rtdb.firebaseio.com/"})


class ProductView(viewsets.ModelViewSet):  
  
  permission_classes = [IsAuthenticated]

  serializer_class = serializers.ProductSerializer
  queryset = models.Producto.objects.all()

  def create(self, request):
    serializer = serializers.ProductSerializer(data=request.data)
    if serializer.is_valid():
      try:
        ref = db.reference('Data')
        data = {
          'nombre': request.data['nombre'],
          'imagen': request.data['imagen'],
          'artesano': request.data['artesano'],
          'precio': request.data['precio'],
          'sku': request.data['sku'],
          'pedidos': False,
          'completado': False,
          'disponible': True
        }
        data_push = ref.push(data)
        
        producto_ref = ref.child(data_push.key)
        producto_ref.update({'id': data_push.key})
        
        res = {
          'created': True,
          'message': 'Se registro correctamente'
        }
        return Response(res, status=status.HTTP_200_OK)
      except:
        res = {
          'created': False,
          'error': 'No se registro el producto'
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    else:
      res = {
        'created': False,
        'error': 'No se registro el producto'
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)


class ListProduct(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, format=None):
    
    ref = db.reference('Data')
    json_data = ref.get()
    data_str = json.dumps(json_data)
    data_dict = json.loads(data_str)
    array_objects = list(data_dict.values())
    return Response(array_objects)
  

class ComprarProduct(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    try:
      ref = db.reference('Data')
      producto_ref = ref.child(request.data['id'])
      producto_ref.update({'pedidos': True})
      producto_ref.update({'disponible': False})
      res = {
            'buy': True,
            'message': 'Pedidos realizado correctamente'
      }
      return Response(res, status=status.HTTP_200_OK)
    except:
      res = {
        'buy': False,
        'error': 'No se completo el pedido'
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)

class CompletarPedido(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    try:
      ref = db.reference('Data')
      producto_ref = ref.child(request.data['id'])
      producto_ref.update({'pedidos': False})
      producto_ref.update({'completado': True})
      res = {
            'Order': True,
            'message': 'Pedidos completado correctamente'
      }
      return Response(res, status=status.HTTP_200_OK)
    except:
      res = {
        'Order': False,
        'error': 'No se completo el pedido'
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)