# Standard Library
from abc import abstractmethod
from typing import Any, Dict

# Internal
from services.domain.customers.models import CustomerData
from services.domain.utils.services import AbstractService


class AbstractServiceCustomer(AbstractService[CustomerData]):
    @abstractmethod
    def get_balance(self, external_id: str) -> Dict[str, Any]:
        pass
