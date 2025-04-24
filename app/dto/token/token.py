from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


@dataclass
class RefreshTokenCreate(BaseModel):
    token: str
    user_oid: UUID
    user_agent: str
    ip_address: str
    expires_at: datetime