# Standard Library
from abc import ABC, abstractmethod
from typing import List

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.domain.utils.repository import AbstractRepository


class AbstractCustomerRepository(AbstractRepository[Customer], ABC):
    """
    Abstract class to define the required customer repository operations.
    """

    @abstractmethod
    def get_customer_loans(self, customer: Customer) -> List[Loan]:
        """
        Retrieves all loans associated with a given customer.

        Args:
            customer (Customer): The customer instance.

        Returns:
            List[Loan]: A list of Loan instances.
        """
        pass

    @abstractmethod
    def get_total_debt(self, customer: Customer) -> float:
        """
        Calculates the total outstanding debt of a given customer.

        Args:
            customer (Customer): The customer instance.

        Returns:
            float: The total debt amount.
        """
        pass
