from django.shortcuts import render
import json
import firebase_admin
from firebase_admin import db, credentials
from rest_framework.views import APIView, Response
from rest_framework import status, viewsets
from usuario import serializers, models


class LoginView(viewsets.ModelViewSet):
  
  serializer_class = serializers.UsuarioSerializer
  queryset = models.Usuario.objects.all()

  def create(self, request):
    serializer = serializers.UsuarioSerializer(data=request.data)
    if serializer.is_valid():
      try:
        ref = db.reference('Usuario')
        json_data = ref.get()
        data_str = json.dumps(json_data)
        data_dict = json.loads(data_str)
        array_objects = list(data_dict.values())
        login = False
        objects = {}
        for i in array_objects:
          if i['email'] == request.data['email']:
            if i['password'] == request.data['password']:
              login = True
              objects = i
        
        res = {
          'login': login,
          'data': objects
        }
        return Response(res, status=status.HTTP_200_OK)
      except:
        res = {
          'login': False,
          'error': 'Usuario o contraseña incorrecta'
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    else:
      res = {
        'login': False,
        'error': 'Usuario o contraseña incorrecta'
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(viewsets.ModelViewSet):

  serializer_class = serializers.UsuarioSerializer
  queryset = models.Usuario.objects.all()

  def create(self, request):
    serializer = serializers.UsuarioSerializer(data=request.data)
    if serializer.is_valid():
      try:
        ref = db.reference('Usuario')
        data = {
          'email': request.data['email'],
          'password': request.data['password'],
          'rol': 'regular',
        }
        data_push = ref.push(data)
        res = {
          'created': True,
          'message': 'Se registro correctamente'
        }
        return Response(res, status=status.HTTP_200_OK)
      except:
        res = {
          'created': False,
          'error': 'No se registro el usuario'
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    else:
      res = {
        'created': False,
        'error': 'No se registro el usuario'
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)