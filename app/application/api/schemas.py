from pydantic import BaseModel


class ErrorResponseSchema(BaseModel):
    error: str
