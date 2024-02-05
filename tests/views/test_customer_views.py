# Standard Library
import os

# Django
from rest_framework import status
from rest_framework.test import APIClient

# Libraries
import pytest

# Internal
from services.django_apps.customers.models import Customer
from tests.factories import CustomerFactory


@pytest.mark.django_db
class TestCustomerViews:
    def setup_method(self):
        self.client = APIClient()
        self.client.credentials(HTTP_X_API_KEY=os.getenv("X_API_KEY"))

    def test_customer_create_view_success(self, api_key):
        payload = {
            "external_id": "external_01",
            "status": 1,
            "score": 700,
        }
        response = self.client.post("/customers/", payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Customer.objects.filter(external_id="external_01").exists()

    def test_customer_create_view_fail_validation(self):
        payload = {
            "external_id": "external_01",
            "status": "invalid",
            "score": 700,
        }
        response = self.client.post("/customers/", payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_customer_balance_view_success(self):
        customer = CustomerFactory(score=700)
        response = self.client.get(f"/customers/{customer.external_id}/balance/")
        assert response.status_code == status.HTTP_200_OK
        assert "available_amount" in response.data

    def test_customer_balance_view_not_found(self):
        response = self.client.get("/customers/non_existing_customer/balance/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
