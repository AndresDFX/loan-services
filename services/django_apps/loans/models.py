# Django
from django.db import models

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.utils.models import BaseModelExternalID
from services.domain.loans.constants import LoanStatus
from services.domain.utils.utils import enum_to_choices


class Loan(BaseModelExternalID):
    customer = models.ForeignKey(Customer, related_name="loans", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.SmallIntegerField(
        choices=enum_to_choices(LoanStatus), default=LoanStatus.ACTIVE
    )
    contract_version = models.CharField(max_length=30, null=True, blank=True)
    maximum_payment_date = models.DateTimeField(null=True, blank=True)
    taken_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.external_id
