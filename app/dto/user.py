from dataclasses import dataclass
from pydantic import BaseModel

from mixins import IntPkMixin, TimeMixin


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    role_id: int
    birthday_date: str


@dataclass
class UserFromDB(UserCreate, IntPkMixin, TimeMixin): ...
