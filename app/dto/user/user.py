from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    birthday_date: datetime
    role_id: int


