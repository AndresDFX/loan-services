# Standard Library
import os
from enum import Enum

X_API_KEY = os.getenv("X_API_KEY", "")


class ApiKeyError(str, Enum):
    NOT_PROVIDED = "x-api-key not provided"
    INVALID = "x-api-key invalid"
