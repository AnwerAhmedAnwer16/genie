from django.apps import AppConfig


class AwtarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awtar'
    verbose_name = 'Awtar'

    def ready(self):
        super().ready()
        from . import extensions  # noqa: F401
