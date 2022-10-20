from email.policy import default
from django.db import models
from django.conf import settings



class AdminApps(models.Model):
    project_name = models.CharField(max_length=50)
    tab_name = models.CharField(max_length=50)
    app_url = models.CharField(max_length=250, null=True, blank=True)
    redirect_path = models.CharField(max_length=250, null=True, blank=True)
    app_order = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name + ' - ' + self.tab_name
    
    class Meta:
        verbose_name = 'Admin App'
        verbose_name_plural = 'Admin Apps'
        unique_together = ('project_name', 'tab_name')