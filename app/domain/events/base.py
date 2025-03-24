from dataclasses import dataclass, field
from abc import ABC
from uuid import UUID, uuid4


@dataclass
class BaseEvent(ABC):
    event_id: UUID = field(default_factory=uuid4, kw_only=True,)