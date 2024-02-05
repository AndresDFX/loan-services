# Current Folder
from . import *

DEBUG = True

ROOT_URLCONF = f"{SITE_NAME}.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("TEST_DATABASE_NAME", "test_database"),
        "USER": environ.get("TEST_DATABASE_USER", "postgres"),
        "PASSWORD": environ.get("TEST_DATABASE_PASSWORD", "admin"),
        "HOST": environ.get("TEST_DATABASE_HOST", "postgres"),
        "PORT": environ.get("TEST_DATABASE_PORT", "5432"),
    }
}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
