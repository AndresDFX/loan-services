# Libraries
import pytest

# Internal
from services.django_apps.payments.adapters.repository import (
    PaymentDetailRepository,
    PaymentRepository,
)
from tests.factories import CustomerFactory, PaymentFactory


@pytest.mark.django_db
class TestPaymentRepository:
    def setup_method(self):
        self.payment_repository = PaymentRepository()
        self.payment_detail_repository = PaymentDetailRepository()

    def test_get_payments_by_customer(self):
        customer = CustomerFactory()
        payment = PaymentFactory(customer=customer)
        payments = self.payment_repository.get_payments_by_customer(customer.external_id)
        assert payment in payments
