from dataclasses import dataclass

from pydantic import BaseModel, EmailStr
from datetime import datetime

from domain.entities.base import BaseEntity


@dataclass(eq=False)
class User(BaseEntity, BaseModel):
    username: str
    role_name: str


@dataclass
class UserInput(BaseEntity, BaseModel):
    username: str
    password: str
    email: EmailStr
    birthday: datetime
    role: str