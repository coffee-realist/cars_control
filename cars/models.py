from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class Car(models.Model):
    """
    Модель, представляющая автомобиль.
    """
    make = models.CharField(max_length=100)  # Марка автомобиля
    model = models.CharField(max_length=100)  # Модель автомобиля
    year = models.IntegerField(  # Год выпуска автомобиля
        validators=[
            MinValueValidator(1886),  # Первый автомобиль в мире
            MaxValueValidator(now().year)  # Текущий год
        ]
    )
    description = models.TextField()  # Описание автомобиля
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Время последнего обновления
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration')  # Владелец автомобиля

    def __str__(self):
        """
        Строковое представление автомобиля.
        """
        return f"{self.make} {self.model} ({self.year})"


class Comment(models.Model):
    """
    Модель, представляющая комментарий к автомобилю.
    """
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания комментария
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')  # Связь с автомобилем
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Автор комментария

    def __str__(self):
        """
        Строковое представление комментария.
        """
        return f"Comment by {self.author.username} on {self.car.make} {self.car.model}"
