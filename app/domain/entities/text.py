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


@dataclass
class TagInput(BaseEntity, BaseModel):
    name: str
    uploader_name: str


@dataclass
class TextInput(BaseEntity, BaseModel):
    value: str
    uploader_name: str
    tags: list[TagInput] = field(default_factory=list)