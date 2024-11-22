from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)  # Регистрация маршрутов для API машин
urlpatterns = [
    path('', include(router.urls)),  # Включение маршрутов API
]
