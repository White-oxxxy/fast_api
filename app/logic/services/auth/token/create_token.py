import jwt

from dataclasses import dataclass

from typing import Union

from domain.services.auth import (
    ICreateTokenService,
    ICreateClaimsService,
)
from settings.dev import CommonSettings
from utils.crypto import load_private_key


@dataclass
class CreateTokenService(ICreateTokenService):
    create_claims_service: ICreateClaimsService
    settings: CommonSettings

    def execute(
            self,
            subject: Union[str, int],
            token_type: str,
            user_claims: dict,
            exp_time: int,
            algorithm: str,
            headers: dict,
    ) -> str:
        claims = self.create_claims_service.execute(
            token_type=token_type,
            subject=subject,
            exp_time=exp_time,
            user_claims=user_claims
        )
        return jwt.encode(
            claims,
            load_private_key(self.settings.jwt_settings.jwt_private_key),
            algorithm=algorithm,
            headers=headers
        )