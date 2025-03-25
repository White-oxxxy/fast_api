from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.text import TextValue
from domain.values.tag import Name


@dataclass(eq=False)
class Tag(BaseEntity):
    name: Name


@dataclass(eq=False)
class Text(BaseEntity):
    value: TextValue
    tags: set[Tag] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_text(self):
        ...

    def get_tag_by_oid(self):
        ...

    def get_tag_by_name(self):
        ...

    def get_text_by_oid(self):
        ...

    def get_text_by_value(self):
        ...

    def get_text_by_tag(self):
        ...

    def tag_fetched(self):
        ...

    def text_fetched(self):
        ...
