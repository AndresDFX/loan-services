# Standard Library
from typing import Any, Dict, TypeVar

# Django
from django.core.exceptions import ValidationError
from rest_framework.request import Request

# Internal
from services.domain.utils import constants
from services.domain.utils.authenticators.base import Authenticator

request_object = TypeVar("request_object", bound=Request)


class ApiKeyAuthenticator(Authenticator):

    def authenticate(self, request: request_object, **kwargs: Dict[str, Any]) -> None:
        api_key = request.META.get("HTTP_X_API_KEY")
        if not api_key:
            raise ValidationError(constants.ApiKeyError.NOT_PROVIDED.value)
        if api_key != constants.X_API_KEY:
            raise ValidationError(constants.ApiKeyError.INVALID.value)
