import jwt

from dataclasses import dataclass

from typing import Union

from domain.services.auth import IDecodeTokenService
from settings.dev import CommonSettings
from utils.crypto import load_public_key
from logic.services.auth.exceptions.exceptions import JWTDecodeException


@dataclass
class DecodeTokenService(IDecodeTokenService):
    settings: CommonSettings

    def execute(self, encoded_token: str) -> dict[str, Union[str, int, bool]]:
        try:
            return jwt.decode(
                encoded_token,
                load_public_key(self.settings.jwt_settings.jwt_public_key),
                leeway=self.settings.jwt_settings.jwt_decode_leeway,
                algorithms=[self.settings.jwt_settings.jwt_decode_algorithm],
            )
        except Exception as err:
            raise JWTDecodeException(status_code=422, message=str(err))