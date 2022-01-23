from .settings import *


DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgresql',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'PORT': 5432,
    }
}