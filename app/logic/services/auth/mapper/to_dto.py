from dataclasses import dataclass

from application.api.auth.schemas.token import CreateRefreshTokenSchema
from dto.token.token_response import RefreshToken as RefreshTokenDto


@dataclass
class FatAPIRequestToRefreshTokenDto:
    @staticmethod
    def execute(request: CreateRefreshTokenSchema) -> RefreshTokenDto:
        return RefreshTokenDto(
            token=request.token,
            username=request.username,
            user_agent=request.user_agent,
            ip_address=request.ip_address,
            expires_at=request.expires_at
        )