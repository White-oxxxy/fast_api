from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class User(BaseModel):
    username: str
    password: str
    birthday_date: str
