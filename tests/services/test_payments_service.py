# Standard Library
from unittest.mock import Mock

# Libraries
import pytest

# Internal
from services.domain.payments.services.services import PaymentService


@pytest.mark.django_db
class TestPaymentService:
    def setup_method(self):
        self.payment_repository_mock = Mock()
        self.payment_detail_repository_mock = Mock()
        self.loan_repository_mock = Mock()
        self.customer_repository_mock = Mock()
        self.payment_service = PaymentService(
            payment_repository=self.payment_repository_mock,
            payment_detail_repository=self.payment_detail_repository_mock,
            loan_repository=self.loan_repository_mock,
            customer_repository=self.customer_repository_mock,
        )

    def test_get_payments_by_customer(self):
        customer_external_id = "some-external-id"
        self.payment_service.get_payments_by_customer(customer_external_id)
        self.payment_repository_mock.get_payments_by_customer.assert_called_once_with(
            customer_external_id
        )
