from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение: только владелец может изменять или удалять запись, остальные имеют доступ только для чтения.
    """

    def has_object_permission(self, request, view, obj):
        # Все пользователи могут читать данные (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Только владелец может редактировать или удалять запись
        return obj.owner == request.user
