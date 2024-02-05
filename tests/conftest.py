# Standard Library
from unittest.mock import Mock

# Libraries
import pytest

# Internal
from services.domain.loans.services.services import LoanService
from services.domain.loans.specifications import (
    LoanAmountWithinCreditLimitSpecification,
)
from tests.factories import CustomerFactory, LoanFactory


@pytest.fixture(scope="session")
def api_key():
    return "api_key_de_prueba"


@pytest.fixture
def customer():
    return CustomerFactory()


@pytest.fixture
def loan(customer):
    return LoanFactory(customer=customer)


@pytest.fixture
def loan_repository_mock():
    return Mock()


@pytest.fixture
def customer_repository_mock():
    return Mock()


@pytest.fixture
def loan_amount_specification_mock():
    return Mock(spec=LoanAmountWithinCreditLimitSpecification)


@pytest.fixture
def loan_service(loan_repository_mock, customer_repository_mock):
    return LoanService(loan_repository_mock, customer_repository_mock)
