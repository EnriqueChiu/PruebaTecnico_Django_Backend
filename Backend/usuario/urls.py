from usuario import views
from django.db import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Login', views.LoginView)
router.register(r'Registro', views.RegisterView)
urlpatterns = router.urls