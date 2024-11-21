from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1886),
            MaxValueValidator(now().year)
        ]
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.car.make} {self.car.model}"
