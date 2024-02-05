# Current Folder
from . import *

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("DATABASE_NAME", "mydatabase"),
        "USER": environ.get("DATABASE_USER", "mydatabaseuser"),
        "PASSWORD": environ.get("DATABASE_PASSWORD", "mypassword"),
        "HOST": environ.get("DATABASE_HOST", "127.0.0.1"),
        "PORT": environ.get("DATABASE_PORT", "5432"),
    }
}

THIRD_PARTY_APPS += ["django_extensions", "debug_toolbar", "drf_yasg"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = ["127.0.0.1"]

DEBUG_TOOLBAR_CONFIG = {"PROFILER_MAX_DEPTH": 30, "SQL_WARNING_THRESHOLD": 100}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
