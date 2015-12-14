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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '  '

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#CRISPY_TEMPLATE_PACK='bootstrap3'

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

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
ABSOLUTE_URL_OVERRIDES = {
    'restaurant.index': lambda o: "/recomet/%s/",
    #'news.story': lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
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


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recomet',
        'USER': 'postgres',
        'PASSWORD':'password',
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
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#CONFIGURACION AGREGADA AL SETTINGS ORIGINAL...................................

STATIC_ROOT ='/static'

#MEDIA_ROOT = '/static/'

STATICFILES_DIRS = (
    '',
    )

# Make this unique, and don't share it with anybody. WEATHER.
SECRET_KEY = ''


TEMPLATE_DIRS = (
    '/root/recomet/templates',
    #os.path.join.dirname(BASE_DIR), "static", "templates",
    )

LOGIN_URL = '/recomet'

#PARA REDIRECCIONAR...
LOGIN_REDIRECT_URL = '/recomet'

AUTH_PROFILE_MODULE = 'restaurant.UserProfile'


EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'email@email.com'

EMAIL_HOST_PASSWORD = ''   #passwd de apps de google

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'email@email.com'

 
 
