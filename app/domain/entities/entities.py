from dataclasses import dataclass, field

from pydantic import BaseModel
from domain.entities.base import BaseEntity


@dataclass
class Role(BaseEntity, BaseModel):
    name: str


@dataclass(eq=False)
class User(BaseEntity, BaseModel):
    username: str
    role_name: str
    active: bool


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


@dataclass(eq=False)
class Action(BaseEntity, BaseModel):
    content: str
    author_name: str
