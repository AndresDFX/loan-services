# Standard Library
import uuid
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar("T")


class AbstractServiceLoan(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity_data: T) -> T:
        pass

    @abstractmethod
    def get_loans_by_customer(self, customer_external_id: uuid.UUID) -> List[T]:
        pass
