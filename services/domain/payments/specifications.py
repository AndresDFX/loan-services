# Django
from django.core.exceptions import ValidationError

# Internal
from services.django_apps.loans.adapters.repository import LoanRepository
from services.domain.payments.models import PaymentData
from services.domain.utils.specification import Specification


class CustomerHasActiveLoansSpecification(Specification):
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    def is_satisfied_by(self, customer_external_id: str) -> bool:
        active_loans = self.loan_repository.get_active_loans_by_customer(customer_external_id)
        if not active_loans:
            raise ValidationError("The customer does not have active loans.")
        return True


class PaymentDoesNotExceedDebtSpecification(Specification):
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    def is_satisfied_by(self, payment_data: PaymentData) -> bool:
        customer_loans = self.loan_repository.get_active_loans_by_customer(
            payment_data.customer_external_id
        )
        total_debt = sum(loan.outstanding for loan in customer_loans)
        if payment_data.total_amount > total_debt:
            raise ValidationError("The payment exceeds the customer's total debt.")
        return True
