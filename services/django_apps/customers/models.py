# Django
from django.db import models

# Internal
from services.django_apps.utils.models import BaseModelExternalID
from services.domain.customers.constants import CustomerStatus
from services.domain.utils.utils import enum_to_choices


class Customer(BaseModelExternalID):
    status = models.SmallIntegerField(
        choices=enum_to_choices(CustomerStatus), default=CustomerStatus.ACTIVE
    )
    score = models.DecimalField(max_digits=12, decimal_places=2)
    preapproved_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.external_id
