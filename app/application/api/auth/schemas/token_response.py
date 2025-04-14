from pydantic import BaseModel


class GetTokenSchema(BaseModel):
    token: str
    used: bool