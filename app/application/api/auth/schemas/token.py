from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class RefreshTokenSchema(BaseModel):
    token: str

class CreateRefreshTokenSchema(BaseModel):
    token: RefreshTokenSchema
    user_id: int
    user_agent: str
    ip_address: str
    expires_at: datetime

class UpdateRefreshTokenSchema(BaseModel):
    used: Optional[bool] = None
    id_address: Optional[str] = None
    user_agent: Optional[str] = None
    expires_at: Optional[datetime] = None