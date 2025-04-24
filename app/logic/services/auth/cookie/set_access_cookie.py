import jwt

from dataclasses import dataclass

from typing import Union
from fastapi import Response

from logic.services.auth.exceptions.exceptions import JWTDecodeException
from domain.services.auth import ICookieService
from settings.dev import CommonSettings
from utils.crypto import load_public_key


@dataclass
class CookieService(ICookieService):
    settings: CommonSettings
    response: Response

    def set_access_cookie(
        self, encoded_access_token: str, max_age: int | None = None
    ) -> None:
        self.response.set_cookie(
            self.settings.jwt_settings.jwt_access_csrf_cookie_key,
            self._decode_token(encoded_access_token)["csrf"],
            max_age=max_age,
            path=self.settings.jwt_settings.jwt_access_csrf_cookie_path,
            domain=self.settings.jwt_settings.jwt_cookie_domain,
            secure=self.settings.jwt_settings.jwt_cookie_secure,
            httponly=False,
            samesite=self.settings.jwt_settings.jwt_cookie_samesite,
        )

    def set_refresh_cookie(
        self, encoded_refresh_token: str, max_age: int | None = None
    ) -> None:
        self.response.set_cookie(
            self.settings.jwt_settings.jwt_refresh_csrf_cookie_key,
            self._decode_token(encoded_refresh_token)["csrf"],
            max_age=max_age,
            path=self.settings.jwt_settings.jwt_refresh_csrf_cookie_path,
            domain=self.settings.jwt_settings.jwt_cookie_domain,
            secure=self.settings.jwt_settings.jwt_cookie_secure,
            httponly=False,
            samesite=self.settings.jwt_settings.jwt_cookie_samesite,
        )

    def _decode_token(self, encoded_token: str) -> dict[str, Union[str, int, bool]]:
        try:
            return jwt.decode(
                encoded_token,
                load_public_key(self.settings.jwt_settings.jwt_public_key),
                leeway=self.settings.jwt_settings.jwt_decode_leeway,
                algorithms=[self.settings.jwt_settings.jwt_decode_algorithm],
            )
        except Exception as err:
            raise JWTDecodeException(status_code=422, message=str(err))

