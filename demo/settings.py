# coding: utf-8
import os


M3_EXT_ROOT = '/home/damirazo/venv/web_bb_new/local/lib/python2.7/site-packages/m3_ext'
M3_ROOT = '/home/damirazo/venv/web_bb_new/local/lib/python2.7/site-packages/m3'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'yunz7!4sczxfx2mur-sec620px!l-(5_+0^o3j&#r!w6&11ubk'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'creadoc',

    'demo.app',
    'demo.app.cars',
    'demo.app.report_settings',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'demo.app.middlewares.FakeUserMiddleware',
)

ROOT_URLCONF = 'demo.urls'
WSGI_APPLICATION = 'demo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join('demo', 'app', 'templates'),
    os.path.join(M3_EXT_ROOT, 'templates'),
    os.path.join(M3_EXT_ROOT, 'ui', 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(M3_EXT_ROOT, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'demo', 'media')
MEDIA_URL = '/downloads/'
