from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import CarSerializer, CommentSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с машинами.
    Позволяет выполнять CRUD-операции (создание, чтение, обновление, удаление).
    """
    queryset = Car.objects.all()  # Все машины из базы данных
    serializer_class = CarSerializer  # Сериализатор для машины
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Права доступа

    def perform_create(self, serializer):
        """
        Автоматически устанавливает текущего пользователя как владельца машины при создании.
        """
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get', 'post'], url_path='comments', permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):
        """
        Обработка комментариев для конкретной машины:
        - GET: Получение списка комментариев.
        - POST: Добавление нового комментария.
        """
        car = self.get_object()  # Получение машины по ID

        if request.method == 'GET':
            # Возвращает все комментарии, связанные с машиной
            comments = car.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            # Создание нового комментария
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(car=car, author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        """
        Возвращает подходящий сериализатор в зависимости от действия.
        Используется CommentSerializer для обработки комментариев.
        """
        if self.action == 'comments':
            return CommentSerializer
        return super().get_serializer_class()


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Представление для удаления машины.
    Доступно только владельцу.
    """
    model = Car  # Модель для удаления
    success_url = '/profile'  # Перенаправление после успешного удаления

    def test_func(self):
        """
        Проверяет, является ли текущий пользователь владельцем машины.
        """
        car = self.get_object()  # Получение машины
        return car.owner == self.request.user
