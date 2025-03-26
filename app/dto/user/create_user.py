from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    birthday_date: str
