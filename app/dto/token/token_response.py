from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime


@dataclass
class RefreshToken(BaseModel):
    token: str
    username: str
    user_agent: str
    ip_address: str
    expires_at: datetime