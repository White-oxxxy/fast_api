from dataclasses import dataclass

from uuid import UUID

from domain.entities.token import RefreshToken
from domain.values.token import (
    TokenName,
    IpAddress,
    UserAgent,
)
from infra.pg.models.user import RefreshTokenORM


@dataclass
class RefreshTokenToRefreshTokenORM:
    @staticmethod
    def execute(token_entity: RefreshToken, user_oid: UUID, role_oid: UUID) -> RefreshTokenORM:
        return RefreshTokenORM(
            token=TokenName(token_entity.token).as_generic_type(),
            user_oid=user_oid,
            role_oid=role_oid,
            user_agent=UserAgent(token_entity.user_agent).as_generic_type(),
            ip_address=IpAddress(token_entity.ip_address).as_generic_type(),
            revoked=token_entity.revoked,
            expires_at=token_entity.expires_at
        )