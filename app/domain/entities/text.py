from dataclasses import dataclass, field
from pydantic import BaseModel

from domain.entities.base import BaseEntity



@dataclass(eq=False)
class Tag(BaseEntity, BaseModel):
    name: str
    uploader_name: str


@dataclass(eq=False)
class Text(BaseEntity, BaseModel):
    value: str
    uploader_name: str
    tags: set[Tag] = field(
        default_factory=set,
        kw_only=True,
    )
