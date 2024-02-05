# Standard Library
import uuid

# Django
from django.utils import timezone

# Libraries
import factory
from factory.django import DjangoModelFactory

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.django_apps.payments.models import Payment, PaymentDetail
from services.domain.customers.constants import CustomerStatus
from services.domain.loans.constants import LoanStatus
from services.domain.payments.constants import PaymentStatus


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    external_id = factory.Sequence(lambda n: f"external_id_{n}")
    status = factory.Iterator([CustomerStatus.ACTIVE, CustomerStatus.INACTIVE])
    score = factory.Faker("pyint", min_value=300, max_value=850)


class LoanFactory(DjangoModelFactory):
    class Meta:
        model = Loan

    external_id = factory.Sequence(lambda n: f"external_id_{n}")
    customer = factory.SubFactory(CustomerFactory)
    amount = factory.Faker("pydecimal", right_digits=2, max_value=10000, positive=True)
    status = factory.Iterator([LoanStatus.PENDING, LoanStatus.ACTIVE, LoanStatus.PAID])
    contract_version = factory.Faker("pystr", min_chars=5, max_chars=10)
    taken_at = factory.LazyFunction(timezone.now)
    outstanding = factory.SelfAttribute("amount")


class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = Payment

    external_id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    customer = factory.SubFactory(CustomerFactory)
    total_amount = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    status = PaymentStatus.COMPLETED
    paid_at = factory.LazyFunction(timezone.now)


class PaymentDetailFactory(DjangoModelFactory):
    class Meta:
        model = PaymentDetail

    payment = factory.SubFactory(PaymentFactory)
    loan = factory.SubFactory(LoanFactory)
    amount = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
