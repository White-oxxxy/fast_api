from dataclasses import dataclass

from datetime import datetime

from .base import BaseEntity
from domain.values.user import (
    Username,
    RoleName,
)
from domain.values.token import (
    TokenName,
    IpAddress,
    UserAgent,
)


@dataclass
class RefreshToken(BaseEntity):
    token: TokenName
    username: Username
    role_name: RoleName
    user_agent: UserAgent
    ip_address: IpAddress
    revoked: bool
    expires_at: datetime

    def update_revoked(self, revoked: bool) -> None:
        self.revoked = revoked
