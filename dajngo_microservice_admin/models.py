from email.policy import default
from django.db import models
from django.conf import settings
from .admin import admin_site



class AdminApps(models.Model):
    app_name = models.CharField(max_length=50, unique=True)
    app_url = models.CharField(max_length=250, unique=True, null=True, blank=True)
    redirect_path = models.CharField(max_length=250, null=True, blank=True)
    app_order = models.IntegerField(default=0)

    def __str__(self):
        return self.app_name
    
    class Meta:
        verbose_name = 'Admin App'
        verbose_name_plural = 'Admin Apps'

admin_site.register(AdminApps)