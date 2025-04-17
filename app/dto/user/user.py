from dataclasses import dataclass
from pydantic import BaseModel, EmailStr
from datetime import datetime


@dataclass
class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    birthday_date: datetime
    role_id: int


