import os
from os.path import join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# One of these will be overwritten at the end of this file
# Depending on whether in production or local
PRODUCTION = False
LOCAL = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

PROJECT_ROOT = './'

MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '*l*t1e2dw24414531@ypxn(^mvty&)^i_d9ch%+rt#+1!4h471'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'starterapp',
    'south',
    'static_management',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

# Static File Management
JS_MEDIA_URL, CSS_MEDIA_URL = [MEDIA_URL] * 2
STATIC_MANAGEMENT_COMPRESS_CMD = 'java -jar %syuicompressor.jar %%s' % PROJECT_ROOT

STATIC_MANAGEMENT = {
    'css': {
        'css/starterapp.min.css': [
            'css/bootstrap.min.css',
            'css/screen.css',
        ],
    },
    'js': {
        'js/starterapp.min.js': [
            'js/bootstrap.min.js',
        ],
    }
}

try:
    from local import *
except ImportError:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
    PRODUCTION = True
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'default_db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    LOCAL = True
