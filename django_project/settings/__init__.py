# Standard Library
import sys
from os import environ
from os.path import abspath, basename, dirname, join, normpath

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

PROJECT_ROOT = dirname(DJANGO_ROOT)

SECRET_KEY = environ.get("SECRET_KEY", "abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_")

SITE_NAME = basename(DJANGO_ROOT)

STATIC_ROOT = join(PROJECT_ROOT, "run", "static")

MEDIA_ROOT = join(PROJECT_ROOT, "run", "images")

STATICFILES_DIRS = []

PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, "services/templates"),
]

sys.path.append(normpath(join(PROJECT_ROOT, "apps")))

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ["rest_framework"]

LOCAL_APPS = [
    "services.django_apps.customers",
    "services.django_apps.loans",
    "services.django_apps.payments",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": PROJECT_TEMPLATES,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

SECRET_FILE = normpath(join(PROJECT_ROOT, "run", "SECRET.key"))

WSGI_APPLICATION = f"{SITE_NAME}.wsgi.application"

ROOT_URLCONF = f"{SITE_NAME}.urls"

SITE_ID = 1

STATIC_URL = "/static/"

MEDIA_URL = "/images/"

DEBUG = False

LANGUAGE_CODE = "en-US"

TIME_ZONE = environ.get("TIME_ZONE", "America/Bogota")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s :: %(asctime)s :: "
            "%(name)s :: %(process)d %(thread)d :: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": environ.get("LOG_LEVEL", "INFO"),
        },
    },
}
