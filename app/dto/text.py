from dataclasses import dataclass
from pydantic import BaseModel

from mixins import IntPkMixin, TimeMixin


@dataclass
class TextCreate(BaseModel):
    value: str
    uploader_name: str


@dataclass
class TagCreate(BaseModel):
    name: str
    uploader_name: str


@dataclass
class TextFromDB(TextCreate, IntPkMixin, TimeMixin): ...


@dataclass
class TagFromDB(TagCreate, IntPkMixin, TimeMixin): ...