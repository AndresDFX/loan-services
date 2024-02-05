# Django
from rest_framework import exceptions as rest_exceptions


class ObjectDoesNotExist(rest_exceptions.ValidationError):
    default_code = "not_found"
