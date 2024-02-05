# Standard Library
from typing import List

# Django
from django.db.models import F

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.domain.loans.constants import LoanStatus
from services.domain.loans.models import LoanData
from services.domain.loans.repository import AbstractLoanRepository


class LoanRepository(AbstractLoanRepository):
    """
    Repository for managing loan data, providing concrete implementations of abstract methods.

    Methods:
        add, get_loans_by_customer, delete, get_by_external_id, list_all, update,
        get_active_loans_by_customer, update_loan_payment.
    """

    def add(self, loan_data: LoanData) -> None:
        customer = Customer.objects.get(external_id=loan_data.customer_external_id)
        loan = Loan(
            external_id=loan_data.external_id,
            customer=customer,
            amount=loan_data.amount,
            outstanding=loan_data.outstanding,
            status=loan_data.status,
        )
        loan.save()

    def get_loans_by_customer(self, customer_external_id: str) -> List[Loan]:
        loans = Loan.objects.filter(customer__external_id=customer_external_id).annotate(
            customer_external_id=F("customer__external_id")
        )
        return list(loans)

    def delete(self, loan_id):
        pass

    def get_by_external_id(self, external_id):
        try:
            return Loan.objects.get(external_id=external_id)
        except Loan.DoesNotExist:
            return None

    def list_all(self):
        return Loan.objects.all()

    def update(self, loan_id, loan_data):
        pass

    def get_active_loans_by_customer(self, customer_external_id: str) -> List[Loan]:
        return Loan.objects.filter(
            customer__external_id=customer_external_id,
            status=LoanStatus.ACTIVE,
        ).order_by("created_at")

    def update_loan_payment(self, loan_id: int, payment_amount: float):
        loan = Loan.objects.get(id=loan_id)
        loan.outstanding -= payment_amount
        loan.status = LoanStatus.PAID if loan.outstanding <= 0 else loan.status
        loan.save()
