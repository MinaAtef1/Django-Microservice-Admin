from enum import unique
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from . import models
from .jwt_serializer import jwt_serializer
import sys

MICROSERVICE_ADMIN_TITLE = getattr(settings, 'MICROSERVICE_ADMIN_TITLE', 'Microservice Admin')


class MicroserviceAdmin(admin.AdminSite):

    def each_context(self, request):
        context = super().each_context(request)
        if not request.user.is_authenticated:
            return context
        microservice_admin_list = []
        for app in models.AdminApps.objects.all().order_by('app_order'):

            human_readable_name = app.tab_name.replace('_', ' ').replace('-', ' ').title()
            unique_app_name = f'app_{app.project_name}_{app.tab_name}'.replace('-', '_').replace(' ', '_')
            if app.project_name == settings.MICROSERVICE_ADMIN_PROJECT_NAME and self.name == app.tab_name:
                app_url = f'{app.app_url}{reverse(f"{app.tab_name}:index")}'
                microservice_admin_list.append({'app_name': human_readable_name, 'app_url': app_url,
                                               'unique_app_name': unique_app_name,  'tab_name': app.tab_name, 'active': True})
            else:
                app_url = f'{app.app_url}{app.redirect_path}'
                microservice_admin_list.append({'app_name': human_readable_name, 'app_url': app_url,
                                               'unique_app_name': unique_app_name, 'tab_name': app.tab_name, 'active': False})

        context["admin_apps"] = microservice_admin_list
        context['microservice_header'] = settings.MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER
        jwt = jwt_serializer.get_token(request.user)
        context['microservice_secret_key'] = jwt
        context['microservice_admin_title'] = MICROSERVICE_ADMIN_TITLE
        return context

    def __init__(self, name, order, include_default_models=True):
        super().__init__(name)

        if 'makemigrations' in sys.argv or 'migrate' in sys.argv:
            return

        if include_default_models:
            from .models import AdminApps
            self.register(User, UserAdmin)
            self.register(Group, GroupAdmin)
            self.register(AdminApps)

        models.AdminApps.objects.get_or_create(
            project_name=settings.MICROSERVICE_ADMIN_PROJECT_NAME,
            tab_name=name,
        )
        models.AdminApps.objects.filter(project_name=settings.MICROSERVICE_ADMIN_PROJECT_NAME, tab_name=name).update(
            app_url=settings.MICROSERVICE_ADMIN_APP_HOST.rstrip('/'),
            redirect_path=settings.MICROSERVICE_REDIRECT_PATH,
            app_order=order,
        )
