from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

from domain.entities.base import BaseEntity


@dataclass(eq=False)
class Role(BaseEntity, BaseModel):
    name: str
    description: Optional[str] = None
