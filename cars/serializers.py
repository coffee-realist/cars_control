from rest_framework import serializers
from .models import Car, Comment


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)