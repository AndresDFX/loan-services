# Standard Library
from typing import List

# Django
from django.core.exceptions import ValidationError

# Internal
from services.django_apps.customers.adapters.repository import (
    CustomerRepository,
)
from services.django_apps.loans.adapters.repository import LoanRepository
from services.domain.loans.models import LoanData
from services.domain.loans.services.base import AbstractServiceLoan
from services.domain.loans.specifications import (
    LoanAmountWithinCreditLimitSpecification,
)


class LoanService(AbstractServiceLoan[LoanData]):
    """
    Service layer for managing loans, including creating and retrieving loans.

    Attributes:
        loan_repository (LoanRepository): Repository for managing loan data.
        customer_repository (CustomerRepository): Repository for managing customer data.
    """

    def __init__(self, loan_repository: LoanRepository, customer_repository: CustomerRepository):
        self.loan_repository = loan_repository
        self.customer_repository = customer_repository
        self.loan_amount_specification = LoanAmountWithinCreditLimitSpecification(
            customer_repository
        )

    def create(self, loan_data: LoanData) -> LoanData:
        """
        Creates a new loan based on provided loan data after checking existing loans and validation.

        Args:
            loan_data (LoanData): The data of the loan to create.

        Returns:
            LoanData: The created loan data.

        Raises:
            ValidationError: If a loan with the same external_id already exists or validation fails.
        """
        existing_loan = self.loan_repository.get_by_external_id(loan_data.external_id)
        if existing_loan is not None:
            raise ValidationError("A loan with this external_id already exists.")

        if self.loan_amount_specification.is_satisfied_by(loan_data):
            self.loan_repository.add(loan_data)
            return loan_data
        else:
            raise Exception("Loan cannot be created due to validation failure.")

    def get_loans_by_customer(self, customer_external_id: str) -> List[LoanData]:
        """
        Retrieves a list of loans associated with a given customer external ID.

        Args:
            customer_external_id (str): The external ID of the customer.

        Returns:
            List[LoanData]: A list of LoanData instances.
        """
        return self.loan_repository.get_loans_by_customer(customer_external_id)
