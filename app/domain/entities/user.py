from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from domain.entities.base import BaseEntity


@dataclass
class Role(BaseEntity, BaseModel):
    name: str
    description: Optional[str] = None


@dataclass(eq=False)
class User(BaseEntity, BaseModel):
    username: str
    password: str
    role_name: str
    birthday: datetime


@dataclass(eq=False)
class Tag(BaseEntity, BaseModel):
    name: str
    uploader_name: str


@dataclass(eq=False)
class Text(BaseEntity, BaseModel):
    value: str
    uploader_name: str
    tags: list[Tag] = field(
        default_factory=list,
        kw_only=True,
    )


@dataclass(eq=False)
class Action(BaseEntity, BaseModel):
    content: str
    author_name: str

