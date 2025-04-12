from dataclasses import dataclass, field

from pydantic import BaseModel
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class Action(BaseEntity, BaseModel):
    content: str
    author_name: str
