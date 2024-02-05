# Standard Library
import os

# Django
from django.core.wsgi import get_wsgi_application

# Current Folder
from .settings import SITE_NAME

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{SITE_NAME}.settings.production")

application = get_wsgi_application()
