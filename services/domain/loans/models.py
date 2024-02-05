# Standard Library
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class LoanData:
    customer_external_id: str
    amount: float
    status: int
    external_id: str = field(default_factory=uuid.uuid4)
    contract_version: Optional[str] = None
    outstanding: float = field(init=False)
    taken_at: Optional[datetime] = datetime.now()

    def __post_init__(self):
        self.outstanding = self.amount
