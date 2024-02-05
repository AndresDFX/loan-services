# Standard Library
from typing import Any

# Django
from django.core.exceptions import ValidationError

# Internal
from services.domain.customers.models import CustomerData
from services.domain.utils.specification import Specification


class ScoreWithinRangeSpecification(Specification[Any]):
    def __init__(self, max_score: int):
        self.max_score = max_score

    def is_satisfied_by(self, candidate: CustomerData) -> bool:
        if candidate.score > self.max_score:
            raise ValidationError(f"Score cannot be greater than {self.max_score}.")
        return True
