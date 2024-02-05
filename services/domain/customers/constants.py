# Standard Library
from enum import Enum


class CustomerStatus(int, Enum):
    ACTIVE = 1
    INACTIVE = 2
