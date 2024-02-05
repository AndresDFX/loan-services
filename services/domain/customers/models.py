# Standard Library
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class CustomerData:
    status: int
    score: float
    preapproved_at: Optional[datetime] = field(default=None)
    external_id: str = field(default_factory=uuid.uuid4)
