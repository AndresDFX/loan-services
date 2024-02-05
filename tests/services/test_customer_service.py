# Standard Library
from unittest.mock import Mock

# Django
from rest_framework.exceptions import ValidationError

# Libraries
import pytest

# Internal
from services.domain.customers.models import CustomerData
from services.domain.customers.services.services import CustomerService
from services.domain.utils.specification import Specification


@pytest.mark.django_db
class TestCustomerService:
    @pytest.fixture
    def customer_repository_mock(self):
        return Mock()

    @pytest.fixture
    def specification_mock(self):
        spec_mock = Mock(spec=Specification)
        spec_mock.is_satisfied_by.return_value = True
        return spec_mock

    def test_create_customer_satisfied_specification(
        self, customer_repository_mock, specification_mock
    ):
        customer_data = CustomerData(
            external_id="external_01",
            status=1,
            score=700,
            preapproved_at=None,
        )

        service = CustomerService(
            repository=customer_repository_mock, specification=specification_mock
        )

        service.create(customer_data)

        customer_repository_mock.add.assert_called_once_with(customer_data)

    def test_create_customer_unsatisfied_specification(
        self, customer_repository_mock, specification_mock
    ):
        specification_mock.is_satisfied_by.return_value = False

        service = CustomerService(
            repository=customer_repository_mock, specification=specification_mock
        )

        with pytest.raises(ValidationError):
            service.create(
                CustomerData(
                    external_id="external_01",
                    status=1,
                    score=500,
                    preapproved_at=None,
                )
            )

    def test_get_balance(self, customer_repository_mock):
        external_id = "external_01"
        customer_data = CustomerData(
            external_id=external_id,
            status=1,
            score=700,
            preapproved_at=None,
        )
        customer_repository_mock.get_by_external_id.return_value = customer_data
        customer_repository_mock.get_total_debt.return_value = 500

        service = CustomerService(repository=customer_repository_mock)

        result = service.get_balance(external_id)

        assert result == {
            "external_id": external_id,
            "score": 700,
            "available_amount": 200,
            "total_debt": 500,
        }
        customer_repository_mock.get_by_external_id.assert_called_once_with(external_id)
        customer_repository_mock.get_total_debt.assert_called_once_with(customer_data)
