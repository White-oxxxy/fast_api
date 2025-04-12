import jwt

from typing import Union
from fastapi import Response

from .exceptions.exceptions import JWTDecodeException
from domain.services.auth import ICookieService
from settings.dev import CommonSettings
from utils.crypto import load_public_key


class CookieService(ICookieService):
    def __init__(self, settings: CommonSettings, response: Response):
        self._config = settings.jwt_settings
        self._response = response

    def set_access_cookie(
        self, encoded_access_token: str, max_age: int | None = None
    ) -> None:
        self._response.set_cookie(
            self._config.jwt_access_csrf_cookie_key,
            self._decode_token(encoded_access_token)["csrf"],
            max_age=max_age,
            path=self._config.jwt_access_csrf_cookie_path,
            domain=self._config.jwt_cookie_domain,
            secure=self._config.jwt_cookie_secure,
            httponly=False,
            samesite=self._config.jwt_cookie_samesite,
        )

    def set_refresh_cookie(
        self, encoded_refresh_token: str, max_age: int | None = None
    ) -> None:
        self._response.set_cookie(
            self._config.jwt_refresh_csrf_cookie_key,
            self._decode_token(encoded_refresh_token)["csrf"],
            max_age=max_age,
            path=self._config.jwt_refresh_csrf_cookie_path,
            domain=self._config.jwt_cookie_domain,
            secure=self._config.jwt_cookie_secure,
            httponly=False,
            samesite=self._config.jwt_cookie_samesite,
        )

    def _decode_token(self, encoded_token: str) -> dict[str, Union[str, int, bool]]:
        try:
            return jwt.decode(
                encoded_token,
                load_public_key(self._config.jwt_public_key),
                leeway=self._config.jwt_decode_leeway,
                algorithms=[self._config.jwt_decode_algorithm],
            )
        except Exception as err:
            raise JWTDecodeException(status_code=422, message=str(err))

