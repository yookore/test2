"""
Django settings for test2 project.

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
SECRET_KEY = '#l_-tuo!a(=5m5(=$9el-2-hd939*5^8r$&llxk@(g91!a8k$2'

# SECURITY WARNING: don't run with debug turned on in production!
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
    'rest_framework',
    'su_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test2.urls'

WSGI_APPLICATION = 'test2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

KEYSPACE_NAME       = 'ks_statusupdate_1'

DATABASES = {
    'default': {
        'ENGINE':       'django.db.backends.sqlite3',
        'NAME':         os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'cassandra': {
        'ENGINE':       'django_cassandra_engine',
        'NAME':         KEYSPACE_NAME,
        'TEST_NAME':    'test_ks_statusupdate',
        'HOST':         '192.168.121.171, 192.168.121.172, 192.168.121.174',    # production
        'USER':         'cassandra',
        'PASSWORD':     'Gonzo@7072',
        'PORT':         9042,
        'OPTIONS': {
            'replication': {
                'strategy_class':       'NetworkTopologyStrategy',
                'DC1':   3
            }
        },

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL   = '/media/'
MEDIA_ROOT  = os.path.join(STATIC_ROOT, 'yookore_media') # Absolute path to the media directory

REST_FRAMEWORK = {
   # 'DEFAULT_PAGINATION_SERIALIZER_CLASS':'statusupdate_app.pagination.YookorePagination',
}

UPM_URL = 'http://upm.apps.yookosapps.com/api/v1/profile/'