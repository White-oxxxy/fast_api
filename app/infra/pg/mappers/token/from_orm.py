from dataclasses import dataclass

from domain.entities.token import RefreshToken
from domain.values.user import (
    Username,
    RoleName,
)
from domain.values.token import (
    TokenName,
    IpAddress,
    UserAgent,
)
from infra.pg.models.user import RefreshTokenORM


@dataclass
class GetRefreshTokenFromORM:
    @staticmethod
    def execute(token_orm: RefreshTokenORM) -> RefreshToken:
        return RefreshToken(
            oid=token_orm.oid,
            token=TokenName(token_orm.token),
            username=Username(token_orm.user.username),
            role_name=RoleName(token_orm.role.name),
            user_agent=UserAgent(token_orm.user_agent),
            ip_address=IpAddress(token_orm.ip_address),
            revoked=token_orm.revoked,
            expires_at=token_orm.expires_at
        )