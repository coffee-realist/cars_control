from rest_framework import serializers
from .models import Car, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['created_at', 'updated_at', 'owner', 'id']

    @staticmethod
    def get_owner(obj):
        return obj.owner.username


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)