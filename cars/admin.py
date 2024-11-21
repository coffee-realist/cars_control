from django.contrib import admin
from .models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'owner', 'created_at', 'updated_at')
    list_filter = ('year', 'make', 'owner')
    search_fields = ('make', 'model', 'owner__username')
    ordering = ('-created_at', 'make',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'car_link', 'author', 'created_at')
    list_filter = ('car__make', 'author')
    search_fields = ('content', 'author__username', 'car__make')
    ordering = ('-created_at',)

    def car_link(self, obj):
        return admin.utils.format_html('<a href="{}">{}</a>', obj.car.get_absolute_url(), obj.car)
    car_link.short_description = "Car"
