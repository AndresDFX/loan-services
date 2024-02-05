# Django
from django.db import models

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.django_apps.utils.models import BaseModelExternalID
from services.domain.payments.constants import PaymentStatus
from services.domain.utils.utils import enum_to_choices


class Payment(BaseModelExternalID):

    customer = models.ForeignKey(Customer, related_name="payments", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.SmallIntegerField(choices=enum_to_choices(PaymentStatus))
    paid_at = models.DateTimeField(null=True, blank=True)


class PaymentDetail(models.Model):
    payment = models.ForeignKey(Payment, related_name="details", on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
