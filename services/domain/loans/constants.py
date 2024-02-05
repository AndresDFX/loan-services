# Standard Library
from enum import IntEnum


class LoanStatus(IntEnum):
    PENDING = 1
    ACTIVE = 2
    REJECTED = 3
    PAID = 4
