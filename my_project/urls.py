from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Административная панель Django
    path('admin/', admin.site.urls),

    # Подключение маршрутов API для работы с машинами и комментариями
    path('api/', include('cars.urls')),

    # Подключение маршрутов для пользовательского интерфейса
    path('', include('user_interface.urls')),
]
