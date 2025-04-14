from dataclasses import dataclass
from pydantic import BaseModel, EmailStr
from datetime import datetime

@dataclass
class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    birthday: datetime
    role: str