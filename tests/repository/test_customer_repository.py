# Django
from django.core.exceptions import ObjectDoesNotExist

# Libraries
import pytest

# Internal
from services.django_apps.customers.adapters.repository import (
    CustomerRepository,
)
from tests.factories import CustomerFactory


@pytest.mark.django_db
class TestCustomerRepository:
    @pytest.fixture(autouse=True)
    def setup_method(self, db):
        self.repository = CustomerRepository()

    def test_add_customer(self):
        new_customer = CustomerFactory.build()
        self.repository.add(new_customer)
        fetched_customer = self.repository.get_by_external_id(new_customer.external_id)
        assert fetched_customer.external_id == new_customer.external_id

    def test_get_by_external_id(self):
        customer = CustomerFactory()
        fetched_customer = self.repository.get_by_external_id(customer.external_id)
        assert fetched_customer.external_id == customer.external_id

    def test_update_customer(self):
        customer = CustomerFactory()
        original_score = customer.score
        customer.score = original_score + 1
        self.repository.update(customer)
        updated_customer = self.repository.get_by_external_id(customer.external_id)
        assert updated_customer.score == original_score + 1

    def test_delete_customer(self):
        customer = CustomerFactory()
        self.repository.delete(customer.external_id)
        with pytest.raises(ObjectDoesNotExist):
            self.repository.get_by_external_id(customer.external_id)

    def test_list_all_customers(self):
        existing_count = len(self.repository.list_all())
        CustomerFactory()
        customers_list = self.repository.list_all()
        assert len(customers_list) == existing_count + 1
