from setuptools import setup, find_packages
from glob import glob


setup(
    name='django-microservice-admin',
    version='0.1.0',
    license='MIT',
    author="Mina Atef",
    author_email='mina.atef0@gmail.com',
    packages=['dajngo_microservice_admin', 'dajngo_microservice_admin.migrations', 'dajngo_microservice_admin.template',]
    data_files = [
        ('migrations', glob('migrations/*')), 
        ('template', glob('template/*')), 
    ],
    
    url='https://github.com/minaaaatef/Django-Microservice-Admin',
    keywords=('django','buttons','admin','actions'),
    install_requires=[
      ],


)