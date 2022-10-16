from setuptools import setup, find_packages
from glob import glob


setup(
    name='django-microservice-admin',
    version='0.1.1',
    license='MIT',
    author="Mina Atef",
    author_email='mina.atef0@gmail.com',
    packages=['django_microservice_admin', 'django_microservice_admin.migrations', 'django_microservice_admin.templates'],
    data_files = [
        ('migrations', glob('migrations/*')), 
        ('templates', glob('templates/*')), 
    ],
    
    url='https://github.com/minaaaatef/Django-Microservice-Admin',
    keywords=('django','buttons','admin','actions'),
    install_requires=[
      ],


)