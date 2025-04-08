from dataclasses import dataclass, field

from pydantic import BaseModel
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class Tag(BaseEntity, BaseModel):
    name: str


@dataclass(eq=False)
class Text(BaseEntity, BaseModel):
    value: str
    tags: list[Tag] = field(
        default_factory=list,
        kw_only=True,
    )