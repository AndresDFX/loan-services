# Standard Library
import uuid
from dataclasses import dataclass
from datetime import datetime

# Libraries
from typing_extensions import Optional


@dataclass
class PaymentData:
    customer_external_id: str
    total_amount: float
    status: int
    id: Optional[int] = None
    customer_id: Optional[int] = None
    paid_at: Optional[datetime] = datetime.now()
    external_id: Optional[str] = str(uuid.uuid4())


@dataclass
class PaymentDetailData:
    payment_id: int
    loan_id: int
    amount: float
