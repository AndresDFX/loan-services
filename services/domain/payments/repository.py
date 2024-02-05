# Standard Library
from abc import ABC, abstractmethod
from typing import List

# Internal
from services.django_apps.payments.models import Payment, PaymentDetail
from services.domain.utils.repository import AbstractRepository


class AbstractPaymentRepository(AbstractRepository[Payment], ABC):
    @abstractmethod
    def get_payments_by_customer(self, customer_external_id: str) -> List[Payment]:
        pass


class AbstractPaymentDetailRepository(AbstractRepository[PaymentDetail], ABC):
    @abstractmethod
    def get_payment_details_by_payment(self, payment_id: str) -> List[PaymentDetail]:
        pass
