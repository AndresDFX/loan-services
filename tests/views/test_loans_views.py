# Django
from rest_framework import status
from rest_framework.test import APIClient

# Libraries
import pytest

# Internal
from services.django_apps.loans.models import Loan
from tests.factories import CustomerFactory, LoanFactory


@pytest.mark.django_db
class TestLoanViews:
    client = APIClient()

    def test_create_loan_success(self):
        customer = CustomerFactory.create()
        loan_data = {
            "external_id": "unique_loan_id_123",
            "customer_external_id": customer.external_id,
            "amount": "100.00",
            "status": 1,
            "contract_version": "v1.0",
        }
        response = self.client.post("/loans/", loan_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Loan.objects.filter(external_id="unique_loan_id_123").exists()

    def test_get_loans_by_customer(self):
        customer = CustomerFactory.create()
        LoanFactory.create(customer=customer, amount="2000.00")
        LoanFactory.create(customer=customer, amount="1500.00")

        response = self.client.get(f"/loans/customer/{customer.external_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
