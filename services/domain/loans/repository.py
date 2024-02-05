# Standard Library
from abc import ABC, abstractmethod
from typing import List

# Internal
from services.django_apps.loans.models import Loan
from services.domain.utils.repository import AbstractRepository


class AbstractLoanRepository(AbstractRepository[Loan], ABC):
    """
    Abstract repository for loan operations, providing the structure for loan-related data management.
    """

    @abstractmethod
    def get_loans_by_customer(self, customer_external_id: str) -> List[Loan]:
        """
        Retrieves a list of loans for a given customer identified by external ID.

        Args:
            customer_external_id (str): The external ID of the customer.

        Returns:
            List[Loan]: A list of Loan instances.
        """
        pass

    @abstractmethod
    def get_active_loans_by_customer(self, customer_external_id: str) -> List[Loan]:
        """
        Retrieves a list of active loans for a given customer identified by external ID.

        Args:
            customer_external_id (str): The external ID of the customer.

        Returns:
            List[Loan]: A list of active Loan instances.
        """
        pass

    @abstractmethod
    def update_loan_payment(self, loan_id: int, payment_amount: float):
        """
        Updates the payment details of a loan.

        Args:
            loan_id (int): The ID of the loan to update.
            payment_amount (float): The amount of payment made.
        """
        pass
