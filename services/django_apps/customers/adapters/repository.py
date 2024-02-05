# Standard Library
from typing import List

# Django
from django.db.models import Sum

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.domain.customers.models import CustomerData
from services.domain.customers.repository import AbstractCustomerRepository


class CustomerRepository(AbstractCustomerRepository):
    def add(self, customer_data: CustomerData) -> None:
        """
        Adds a new customer to the database.

        Args:
            customer_data (CustomerData): Data transfer object
            containing customer information.
        """
        customer = Customer(
            external_id=customer_data.external_id,
            status=customer_data.status,
            score=customer_data.score,
            preapproved_at=customer_data.preapproved_at,
        )
        customer.save()

    def get_by_external_id(self, external_id: str) -> Customer:
        """
        Retrieves a customer by their external ID.

        Args:
            external_id (str): The external ID of the customer.

        Returns:
            Customer: The customer instance.
        """
        return Customer.objects.get(external_id=external_id)

    def update(self, customer: Customer) -> None:
        """
        Updates a customer in the database.

        Args:
            customer (Customer): The customer instance to update.
        """
        customer.save()

    def delete(self, external_id: str) -> None:
        """
        Deletes a customer from the database by their external ID.

        Args:
            external_id (str): The external ID of the customer.
        """
        Customer.objects.filter(external_id=external_id).delete()

    def list_all(self) -> List[Customer]:
        """
        Lists all customers in the database.

        Returns:
            List[Customer]: A list of all customer instances.
        """
        return list(Customer.objects.all())

    def get_customer_loans(self, customer: Customer) -> List[Loan]:
        """
        Retrieves all loans associated with a given customer.

        Args:
            customer (Customer): The customer instance.

        Returns:
            List[Loan]: A list of Loan instances.
        """
        return Loan.objects.filter(customer=customer)

    def get_total_debt(self, customer: Customer) -> float:
        """
        Calculates the total outstanding debt of a given customer.

        Args:
            customer (Customer): The customer instance.

        Returns:
            float: The total debt amount.
        """
        return (
            Loan.objects.filter(customer=customer).aggregate(total=Sum("outstanding"))["total"]
            or 0.0
        )
