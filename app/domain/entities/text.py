from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.text import TagName, TextValue
from domain.values.user import Username


@dataclass
class Tag(BaseEntity):
    name: TagName


@dataclass
class Text(BaseEntity):
    value: TextValue
    tags: list[Tag] = field(
        default_factory=list,
        kw_only=True,
    )


@dataclass
class TagInput(BaseEntity):
    name: TagName
    uploader_name: Username


@dataclass
class TextInput(BaseEntity):
    value: TextValue
    uploader_name: Username
    tags: list[TagInput] = field(default_factory=list)

