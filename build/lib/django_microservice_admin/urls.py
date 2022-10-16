# urls.py

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import microservice_admin_view


urlpatterns = [
    path('microservice_admin/', csrf_exempt(microservice_admin_view), name='microservice_admin_view'),
]