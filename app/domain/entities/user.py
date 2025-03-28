from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from domain.entities.base import BaseEntity

@dataclass(eq=False)
class User(BaseEntity, BaseModel):
    username: str
    password: str
    role_id: UUID
    birthday: datetime

