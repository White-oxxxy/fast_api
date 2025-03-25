from dataclasses import dataclass, field
from datetime import datetime, timezone
from abc import ABC
from uuid import UUID, uuid4


@dataclass
class BaseEvent(ABC):
    event_id: UUID = field(default_factory=uuid4, kw_only=True)
    occurred_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc), kw_only=True
    )
