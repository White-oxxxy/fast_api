from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel


@dataclass
class RefreshTokenCreate(BaseModel):
    token: str
    user_id: int
    user_agent: str
    ip_address: str
    expires_at: datetime

@dataclass
class GetRefreshToken(BaseModel):
    token: str
    expires_at: datetime