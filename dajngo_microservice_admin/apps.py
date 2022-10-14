from django.db import OperationalError
from django.db import transaction
from django.apps import AppConfig
from django.conf import settings
import sys
from django.urls import reverse

class MicroserviceAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservice_admin'

    @transaction.atomic
    def ready(self):

        if 'makemigrations' in sys.argv or 'migrate' in sys.argv:
            return

        from .models import AdminApps

        MICROSERVICE_ADMIN_APP_VARS = ['MICROSERVICE_ADMIN_APP_NAME', 'MICROSERVICE_ADMIN_APP_HOST', 'MICROSERVICE_ADMIN_APP_ORDER']

        for var in MICROSERVICE_ADMIN_APP_VARS:
            if not hasattr(settings, var):
                raise Exception(f"Missing {var} in settings.py")
        

            AdminApps.objects.get_or_create(
                app_name=settings.MICROSERVICE_ADMIN_APP_NAME,
            )

            AdminApps.objects.filter(app_name=settings.MICROSERVICE_ADMIN_APP_NAME).update(
                app_url=settings.MICROSERVICE_ADMIN_APP_HOST.rstrip('/'),
                redirect_path = reverse('microservice_admin_view'),
                app_order=settings.MICROSERVICE_ADMIN_APP_ORDER,
            )