"""
Django settings for recomet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
    'registration',
    'django_countries',
)

ACCOUNT_ACTIVATION_DAYS = 7 
ABSOLUTE_URL_OVERRIDES = {
    'restaurant.index': lambda o: "/recomet/%s/",
}
REGISTRATION_OPEN=True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recomet.urls'
WSGI_APPLICATION = 'recomet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recomet',
        'USER': 'postgres',
        'PASSWORD':'admin',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


#CONFIGURACION AGREGADA AL SETTINGS

STATIC_ROOT ='/static'
STATICFILES_DIRS = (
    '',
    )

# Make this unique, and don't share it with anybody. WEATHER.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#    #'django.template.loaders.eggs.load_template_source',
#)
TEMPLATE_DIRS = (
    '/root/recomet/templates',
    )

LOGIN_URL = '/recomet'
LOGIN_REDIRECT_URL = '/recomet'
AUTH_PROFILE_MODULE = 'restaurant.UserProfile' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'x@gmail.com'
EMAIL_HOST_PASSWORD = ''  
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'x@gmail.com'

 
 
