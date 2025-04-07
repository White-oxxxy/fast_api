from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr | None = None
    active: bool = False
    roles = list[str]


class UserLogin(BaseModel):
    login: str
    password: str
