from django.apps import AppConfig


class YallaThailandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yalla_thailand'
    verbose_name = 'Yalla Thailand'

    def ready(self):
        super().ready()
        from . import extensions  # noqa: F401
