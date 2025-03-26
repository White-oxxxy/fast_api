from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.text import TextValue
from domain.values.tag import Name


@dataclass(eq=False)
class Tag(BaseEntity):
    name: Name
    uploader_name: str


@dataclass(eq=False)
class Text(BaseEntity):
    value: TextValue
    uploader_name: str
    tags: set[Tag] = field(
        default_factory=set,
        kw_only=True,
    )
