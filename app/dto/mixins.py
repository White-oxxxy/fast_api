from dataclasses import dataclass
from datetime import datetime


@dataclass
class IntPkMixin:
    pk: int


@dataclass
class TimeMixin:
    create_at: datetime
    update_at: datetime
