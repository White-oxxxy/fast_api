from pydantic import BaseModel


class GetUserDetailSchema(BaseModel):
    active: bool
    role: str