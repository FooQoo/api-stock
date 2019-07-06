from .base_settings import *
from os import environ
import django_heroku

DEBUG = False

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ['NAME'],
        'HOST': environ['HOST'],
        'USER': environ['USER'],
        'PORT': environ['PORT'],
        'PASSWORD': environ['PASSWORD'],
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
                    'charset': 'utf8mb4',
                },
    }
}

# env
SECRET_KEY = environ['SECRET_KEY']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
django_heroku.settings(locals())
