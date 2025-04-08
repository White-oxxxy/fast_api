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