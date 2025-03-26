from dataclasses import dataclass
from typing import Optional

from domain.entities.base import BaseEntity
from domain.values.role import Name


@dataclass(eq=False)
class Role(BaseEntity):
    name: Name
    description: Optional[str] = None
