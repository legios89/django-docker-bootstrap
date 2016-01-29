# coding: utf-8
# Core and 3th party packages
import os
from django.utils.translation import ugettext_lazy as _


def getvar(name, default=None, required=True):
    """
    Returns the value of an environment variable.
    If the variable is not present, default will be used.
    If required is True, only not None values will be returned,
    will raise an exception instead of returning None.
    """
    ret = os.environ.get(name, default)
    if required and ret is None:
        raise Exception('Environment variable %s is not set' % name)
    return ret


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = getvar('DJANGO_SECRET_KEY')
DEBUG = getvar('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = getvar('ALLOWED_HOSTS', '').split(',')
LOGIN_URL = '/admin/login/'

# Application definition
INSTALLED_APPS = (
    # django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'debug_toolbar',
    # project apps
    'core',
    {%- if cookiecutter.use_translation == 'True' %}
    # 3rd party
    'rosetta',
    {%- endif %}
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    {% if cookiecutter.use_translation == 'True' -%}
    'django.middleware.locale.LocaleMiddleware',
    {% endif -%}
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'postgres',
        'PORT': '5432',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': getvar('DB_PASSWORD')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

LANGUAGE_CODE = 'en'
LANGUAGES = [('en', _('English'))]
{% if cookiecutter.use_translation == 'True' -%}
LOCALE_PATHS = ('/data/locale/',)
if getvar('YANDEX_TRANSLATE_KEY', required=False):
    ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
    YANDEX_TRANSLATE_KEY = getvar('YANDEX_TRANSLATE_KEY')
{%- endif %}

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = '/data/static/'

# Debug toolbar visibility fix
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda x: DEBUG,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}
