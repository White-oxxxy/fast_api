from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime

from mixins import IntPkMixin, TimeMixin


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role_id: int
    birthday_date: datetime


@dataclass
class User(BaseModel):
    username: str
    password: str
    birthday: datetime


@dataclass
class UserFromDB(UserCreate, IntPkMixin, TimeMixin): ...
