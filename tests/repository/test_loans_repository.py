# Standard Library
from decimal import Decimal

# Libraries
import pytest

# Internal
from services.django_apps.loans.adapters.repository import LoanRepository
from tests.factories import CustomerFactory, LoanFactory


@pytest.mark.django_db
class TestLoanRepository:
    def setup_method(self):
        self.repository = LoanRepository()

    def test_get_loans_by_customer(self):
        customer = CustomerFactory()
        loan = LoanFactory(customer=customer)
        loans = self.repository.get_loans_by_customer(customer.external_id)
        assert loan in loans

    def test_update_loan_payment(self):
        loan = LoanFactory()
        payment_amount = Decimal("100.00")
        self.repository.update_loan_payment(loan.id, payment_amount)
        loan.refresh_from_db()
        assert loan.outstanding == loan.amount - payment_amount
