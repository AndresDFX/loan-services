# Standard Library
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

# Internal
from services.domain.customers.models import CustomerData


class Authenticator(ABC):

    @abstractmethod
    def authenticate(self, request: Any, **kwargs: Dict[str, Any]) -> Optional[CustomerData]:
        pass
