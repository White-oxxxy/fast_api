from dataclasses import dataclass

from .create_text import TagCreate, TextCreate
from ..mixins import IntPkMixin, TimeMixin


@dataclass
class TextFromDB(TextCreate, IntPkMixin, TimeMixin): ...


@dataclass
class TagFromDB(TagCreate, IntPkMixin, TimeMixin): ...
