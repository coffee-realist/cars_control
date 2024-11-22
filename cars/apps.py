from django.apps import AppConfig


class CarsConfig(AppConfig):
    """
    Конфигурация приложения Cars.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
