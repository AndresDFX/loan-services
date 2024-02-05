# Standard Library
from decimal import Decimal
from typing import Any, Dict

# Django
from rest_framework.exceptions import ValidationError

# Internal
from services.domain.customers.models import CustomerData
from services.domain.customers.repository import AbstractCustomerRepository
from services.domain.customers.services.base import AbstractServiceCustomer
from services.domain.utils.specification import Specification


class CustomerService(AbstractServiceCustomer):
    """
    Provides service layer functionalities for
    customer operations,
    including creating a customer
    and retrieving customer balance information.

    Attributes:
        repository (AbstractCustomerRepository): The customer repository for database operations.
        specification (Specification[CustomerData], optional): A specification to validate the customer data.
    """

    def __init__(
        self,
        repository: AbstractCustomerRepository,
        specification: Specification[CustomerData] = None,
    ):
        self.repository = repository
        self.specification = specification

    def create(self, customer_data: CustomerData) -> CustomerData:
        """
        Creates a new customer based on the provided customer data after validating against specifications.

        Args:
            customer_data (CustomerData): The data of the customer to create.

        Returns:
            CustomerData: The created customer data.

        Raises:
            ValidationError: If the customer data does not satisfy the specifications.
        """
        if self.specification and not self.specification.is_satisfied_by(customer_data):
            raise ValidationError("Customer does not meet the specified criteria.")

        self.repository.add(customer_data)
        return customer_data

    def get_balance(self, external_id: str) -> Dict[str, Any]:
        """
        Retrieves the balance information for a customer identified by the external ID.

        Args:
            external_id (str): The external ID of the customer.

        Returns:
            Dict[str, Any]: A dictionary containing the customer's external ID, score, available amount, and total debt.
        """
        customer_data = self.repository.get_by_external_id(external_id)
        total_debt = Decimal(self.repository.get_total_debt(customer_data))
        available_amount = customer_data.score - total_debt
        return {
            "external_id": str(customer_data.external_id),
            "score": customer_data.score,
            "available_amount": available_amount,
            "total_debt": total_debt,
        }
