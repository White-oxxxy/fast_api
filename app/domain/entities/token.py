from dataclasses import dataclass

from datetime import datetime

from .base import BaseEntity


@dataclass
class Token(BaseEntity):
    token: str
    expires_at: datetime

