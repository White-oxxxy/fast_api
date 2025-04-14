from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role_id: int
    birthday_date: datetime


