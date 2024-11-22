from django.contrib import admin
from .models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления моделью Car.
    """
    list_display = ('make', 'model', 'year', 'owner', 'created_at', 'updated_at')  # Отображаемые поля
    list_filter = ('year', 'make', 'owner')  # Фильтры для удобства поиска
    search_fields = ('make', 'model', 'owner__username')  # Поля для поиска
    ordering = ('-created_at', 'make',)  # Порядок сортировки


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления моделью Comment.
    """
    list_display = ('content', 'car_link', 'author', 'created_at')  # Отображаемые поля
    list_filter = ('car__make', 'author')  # Фильтры для удобства поиска
    search_fields = ('content', 'author__username', 'car__make')  # Поля для поиска
    ordering = ('-created_at',)  # Порядок сортировки

    def car_link(self, obj):
        """
        Возвращает ссылку на машину, к которой относится комментарий.
        """
        return admin.utils.format_html('<a href="{}">{}</a>', obj.car.id, obj.car)

    car_link.short_description = "Car"
    car_link.admin_order_field = 'car'  # Поле для сортировки
