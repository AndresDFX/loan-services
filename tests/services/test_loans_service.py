# test_loan_service.py

# Standard Library
from unittest.mock import Mock

# Django
from django.core.exceptions import ValidationError

# Libraries
import pytest

# Internal
from services.domain.loans.constants import LoanStatus
from services.domain.loans.models import LoanData
from services.domain.loans.services.services import LoanService
from services.domain.loans.specifications import (
    LoanAmountWithinCreditLimitSpecification,
)


@pytest.mark.django_db
class TestLoanService:
    @pytest.fixture
    def loan_repository_mock(self):
        return Mock()

    @pytest.fixture
    def customer_repository_mock(self):
        return Mock()

    @pytest.fixture
    def specification_mock(self):
        spec_mock = Mock(spec=LoanAmountWithinCreditLimitSpecification)
        spec_mock.is_satisfied_by.return_value = True
        return spec_mock

    def test_create_loan_with_existing_external_id_raises_error(
        self, loan_repository_mock, customer_repository_mock
    ):
        loan_repository_mock.get_by_external_id.return_value = LoanData(
            external_id="loan_01",
            customer_external_id="external_01",
            amount=1000.00,
            status=LoanStatus.ACTIVE,
        )

        service = LoanService(
            loan_repository=loan_repository_mock,
            customer_repository=customer_repository_mock,
        )

        with pytest.raises(ValidationError):
            service.create(
                LoanData(
                    external_id="loan_01",
                    customer_external_id="external_01",
                    amount=500.00,
                    status=LoanStatus.ACTIVE,
                )
            )

    def test_get_loans_by_customer(self, loan_repository_mock, customer_repository_mock):
        customer_external_id = "external_01"
        service = LoanService(
            loan_repository=loan_repository_mock,
            customer_repository=customer_repository_mock,
        )

        service.get_loans_by_customer(customer_external_id)

        loan_repository_mock.get_loans_by_customer.assert_called_once_with(customer_external_id)
