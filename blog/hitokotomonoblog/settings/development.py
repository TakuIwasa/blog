from .base import *

DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hitokotomonoblogdb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
}