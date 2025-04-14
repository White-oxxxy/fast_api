from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    birthday: datetime
    active: bool = False
    roles = list[str]


class UserLogin(BaseModel):
    login: str
    password: str

class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
    birthday: datetime
    role: str