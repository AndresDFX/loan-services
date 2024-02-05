# Django
from django.core.exceptions import ValidationError

# Internal
from services.django_apps.customers.adapters.repository import (
    CustomerRepository,
)
from services.domain.loans.models import LoanData
from services.domain.utils.specification import Specification


class LoanAmountWithinCreditLimitSpecification(Specification[LoanData]):
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def is_satisfied_by(self, candidate: LoanData) -> bool:
        customer = self.customer_repository.get_by_external_id(candidate.customer_external_id)
        total_loans_amount = sum(
            loan.amount for loan in self.customer_repository.get_customer_loans(customer)
        )

        available_amount = customer.score - total_loans_amount

        if candidate.amount > available_amount:
            raise ValidationError(
                "The amount of the new loan exceeds the customer's " "available credit limit."
            )

        return True
