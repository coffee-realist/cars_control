from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения данных о пользователе.
    """
    class Meta:
        model = User
        fields = ['username']


class CarSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Car.
    """
    owner = serializers.SerializerMethodField()  # Преобразование поля owner в строковое представление

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['created_at', 'updated_at', 'owner', 'id']

    @staticmethod
    def get_owner(obj):
        """
        Возвращает имя владельца или 'Аноним', если данные отсутствуют.
        """
        first_name = obj.owner.first_name
        last_name = obj.owner.last_name
        if first_name and last_name:
            return f"{first_name} {last_name[0]}."
        elif first_name:
            return f"{first_name[0]}."
        else:
            return "Аноним"


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    """
    author = serializers.SerializerMethodField()  # Преобразование поля author в строковое представление

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']
        read_only_fields = ['author', 'created_at', 'car']

    @staticmethod
    def get_author(obj):
        """
        Возвращает имя автора или 'Аноним', если данные отсутствуют.
        """
        first_name = obj.author.first_name
        last_name = obj.author.last_name
        if first_name and last_name:
            return f"{first_name} {last_name[0]}."
        elif first_name:
            return f"{first_name[0]}."
        else:
            return "Аноним"
