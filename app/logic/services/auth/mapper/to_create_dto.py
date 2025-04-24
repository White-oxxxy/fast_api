from dataclasses import dataclass
from uuid import UUID

from dto.token.token_response import RefreshToken
from dto.token.token import RefreshTokenCreate


@dataclass
class RefreshTokenDtoToRefreshTokenCreate:
    @staticmethod
    def execute(token_dto: RefreshToken, user_oid: UUID) -> RefreshTokenCreate:
        return RefreshTokenCreate(
            token=token_dto.token,
            user_oid=user_oid,
            user_agent=token_dto.user_agent,
            ip_address=token_dto.ip_address,
            expires_at=token_dto.expires_at,
        )