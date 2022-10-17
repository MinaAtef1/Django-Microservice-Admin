# Django Microservice Admin
## Introduction
<p align="center">
<img  src="https://user-images.githubusercontent.com/36309814/196048602-78de66a3-9e90-4598-bc77-6b4c4cb943fd.png">
</p>


This package helps connect the admin app for multiple django projects,
all the apps will only share the settings, users, permissions
and each app will have its separate database 

![image](https://user-images.githubusercontent.com/36309814/196048158-bd327cbf-a362-4651-9ff5-c6155c6b86bd.png)

## Requirements
This app uses 
- Django Rest Framework [install from here](https://www.django-rest-framework.org/#installation)
- Django Rest Framework Simple jwt [install from here](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)


## How does it work
Each app will register itself when it starts, once it's registered it will appear as a tab in the admin navbar, 
on clicking on one of the other apps, a post request is then made, that sends the jwt of the user to the other app, which logs in the user in the other app, making the experience as smooth as possible

## Getting Started
- Install the package
```
pip install django-microservice-admin
```

- Add the package to the installed apps above the admin package
```python
INSTALLED_APPS = [
    'Main',
    'django_microservice_admin', #<----- add here 
    'django.contrib.admin',
]
```
- Make sure you have `templates` in the templates directory
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
- Add the urls to the app urls
``` python
from django_microservice_admin.admin import admin_site
urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('django_microservice_admin.urls')),
    ...
]
```
- Add settings Configuration 
```

MICROSERVICE_ADMIN_APP_NAME = 'first app'
MICROSERVICE_ADMIN_APP_HOST = "http://127.0.0.1:8000/"
MICROSERVICE_ADMIN_APP_ORDER = 1
MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER = "X-MSA-SECRET-KEY"
MICROSERVICE_ADMIN_REGISTER_SETTINGS = True
MICROSERVICE_ADMIN_TITLE = "Microservice Admin"

```
| MICROSERVICE_ADMIN_APP_NAME   | Required/default     | The app name that appears on the navbar, each app should have a unique name    |
| --- | --- | --- |
| MICROSERVICE_ADMIN_APP_HOST      | REQUIRED   | The link to the app host    |
| MICROSERVICE_ADMIN_APP_ORDER     | REQUIRED   | The navbar order for the app|
| MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER     | REQUIRED   | The header name that is used for the jwt in the form, should be the same for all the apps|
| MICROSERVICE_ADMIN_REGISTER_SETTINGS     | default = False   | is the app used to show the settings table (users, permissions,etc...)|
|MICROSERVICE_ADMIN_TITLE| REQUIRED | The app name that appears on the admin nav|

- Migrate Database
Note: the package uses the default database, which should have the users, permissions, etc...
``` 
python manage.py migrate
```
- Start using the admin

The package provides its own instance of the admin
```python 
from django_microservice_admin.admin import admin_site

admin_site.register(model)
```
