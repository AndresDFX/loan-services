# Standard Library
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar("T")


class AbstractServicePayment(ABC, Generic[T]):
    @abstractmethod
    def create_payment(self, payment_data: T) -> T:
        pass

    @abstractmethod
    def get_payments_by_customer(self, customer_external_id: str) -> List[T]:
        pass
