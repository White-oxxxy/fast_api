from dataclasses import dataclass

from dto.token.token import GetRefreshToken
from infra.pg.models.user import RefreshTokenORM


@dataclass
class GetTokenFromORM:
    @staticmethod
    def execute(token: RefreshTokenORM) -> GetRefreshToken:
        return GetRefreshToken(
            token=token.token,
            expires_at=token.expires_at
        )