from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение: только владелец может изменять или удалять запись, остальные имеют доступ только для чтения.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет права доступа к объекту:
        - Все пользователи могут читать данные (GET, HEAD, OPTIONS).
        - Только владелец может редактировать или удалять запись.
        """
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.owner == request.user
