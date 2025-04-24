from dataclasses import dataclass

from dto.token.token import RefreshTokenCreate
from infra.pg.models.user import RefreshTokenORM


@dataclass
class CreateRefreshTokenORM:
    @staticmethod
    def execute(token: RefreshTokenCreate) -> RefreshTokenORM:
        return RefreshTokenORM(
            token=token.token,
            user_oid=token.user_oid,
            user_agent=token.user_agent,
            ip_address=token.ip_address,
            expires_at=token.expires_at
        )