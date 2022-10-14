import secrets
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import AdminApps
from rest_framework_simplejwt.backends import TokenBackend

def microservice_admin_view(request):
    if request.method == 'POST':
        if settings.MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER not in  request.POST:
            return HttpResponse('No Key', status=403)

        jwt_secret_key = request.POST[settings.MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER]
        
        try:
            valid_data = TokenBackend(
                    algorithm='HS256',signing_key=settings.SECRET_KEY).decode(jwt_secret_key, verify=True)

        except:
            return HttpResponse('Invalid Key', status=403)

        user = get_user_model().objects.get(id=valid_data['user_id'])

        login(request, user)

        return redirect(reverse('admin:index'))