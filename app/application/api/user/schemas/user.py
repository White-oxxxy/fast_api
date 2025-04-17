from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    birthday: datetime
    active: bool = False
    roles = list[str]


class UserLoginSchema(BaseModel):
    login: str
    password: str


class AccessTokenLoginResponseSchema(BaseModel):
    access_token: str


class AccessTokenRegisterResponseSchema(BaseModel):
    access_token: str
    role: str


class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
    birthday: datetime
    role: str


