from django.urls import path
from .views import register, custom_logout
from .views import profile, home
from cars.views import CarDeleteView

from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>/', profile, name='edit-car'),  # Редактирование автомобиля
    path('profile/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),  # Удаление автомобиля
    path('', home, name='home'),
]
