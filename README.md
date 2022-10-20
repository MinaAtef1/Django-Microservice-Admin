# Django Microservice Admin
## Introduction
<p align="center">
<img  src="https://user-images.githubusercontent.com/36309814/196048602-78de66a3-9e90-4598-bc77-6b4c4cb943fd.png">
</p>


This package helps connect the admin app for multiple django projects,
all the apps will only share the settings, users, permissions
and each app will have its separate database 

![image](https://user-images.githubusercontent.com/36309814/196048158-bd327cbf-a362-4651-9ff5-c6155c6b86bd.png)


## How does it work
Each app will register itself when it starts, once it's registered it will appear as a tab in the admin navbar, 
on clicking on one of the other apps, a post request is then made, that sends the jwt of the user to the other app, which logs in the user in the other app, making the experience as smooth as possible


## Requirements
This app uses 
- Django Rest Framework [install from here](https://www.django-rest-framework.org/#installation)
- Django Rest Framework Simple jwt [install from here](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)

## Getting Started
### Install the package
```
pip install django-microservice-admin
```

### Add the package to the installed apps above the admin package
```python
INSTALLED_APPS = [
    'django_microservice_admin', #<----- add here 
    'django.contrib.admin',
]
```

### Make sure you have `templates` in the templates directory
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # <---- this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


### Add settings Configuration 
```

MICROSERVICE_ADMIN_PROJECT_NAME = 'first app'
MICROSERVICE_ADMIN_APP_HOST = "http://127.0.0.1:8000/"
MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER = "X-MSA-SECRET-KEY"
MICROSERVICE_ADMIN_TITLE = "Microservice Admin"
MICROSERVICE_REDIRECT_PATH = "/microservice_admin/"

```
| Configuration   | Required/default     | Description  |
| --- | --- | --- |
| MICROSERVICE_ADMIN_PROJECT_NAME      | REQUIRED   | The name of the project|
| MICROSERVICE_ADMIN_APP_HOST     | REQUIRED   | The url of the site|
| MICROSERVICE_REDIRECT_PATH     | REQUIRED   | the path to the microservice_view, ex: '/microservice_admin/' |
| MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER     | REQUIRED   | The header name that is used for the jwt in the form, should be the same for all the apps|
| MICROSERVICE_ADMIN_TITLE     | REQUIRED   | The title that shown in the admin |

### Migrate Database
Note: the package uses the default database, which should have the users, permissions, etc...
``` 
python manage.py migrate
```
### Create admin site instance
The same project can have multiple taps, you just have to make an instance for each tab.
```
# admin.py
from django_microservice_admin.admin import MicroserviceAdmin
admin_site = MicroserviceAdmin(name='admin', order=1, include_default_models=True)
```

| Arg   | Required/default     | Description    |
| --- | --- | --- |
| name| REQUIRED   | The name of the tab    |
| order     | REQUIRED   | The order of the tabs|
| include_default_models     | default=True   | whether to add the default models(users, groups, etc...)|

### Add the urls to the app urls
``` python
from .admin import admin_site
urlpatterns = [
    path('admin/', admin_site.urls),
    path('microservice_admin/', include('django_microservice_admin.urls')),
    ...
]
```
