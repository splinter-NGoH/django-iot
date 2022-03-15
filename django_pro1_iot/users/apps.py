from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "django_pro1_iot.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import django_pro1_iot.users.signals  # noqa F401
        except ImportError:
            pass
