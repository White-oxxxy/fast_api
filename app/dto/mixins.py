from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class UUIDPkMixin:
    pk: UUID


@dataclass
class TimeMixin:
    create_at: datetime
    update_at: datetime
