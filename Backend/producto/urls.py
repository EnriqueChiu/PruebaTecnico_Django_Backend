from producto import views
from django.urls import path, include

from django.db import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'RegistrarProducto', views.ProductView)
#urlpatterns = router.urls



urlpatterns = [
  path(r'ObtenerProducto', views.ListProduct.as_view()),
  path(r'ComprarProducto', views.ComprarProduct.as_view()),
  path(r'CompletarPedido', views.CompletarPedido.as_view()),
  path(r'', include(router.urls)),
]