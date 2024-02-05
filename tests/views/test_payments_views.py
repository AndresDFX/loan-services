# Django
from django.urls import reverse
from rest_framework.test import APIClient

# Libraries
import pytest

# Internal
from tests.factories import CustomerFactory, PaymentFactory


@pytest.mark.django_db
class TestPaymentViews:
    def setup_method(self):
        self.client = APIClient()

    def test_payments_by_customer_view(self):
        customer = CustomerFactory()
        PaymentFactory(customer=customer)
        url = reverse("payments-by-customer", kwargs={"customer_external_id": customer.external_id})
        response = self.client.get(url)
        assert response.status_code == 200
