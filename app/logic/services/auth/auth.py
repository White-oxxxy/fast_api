from datetime import datetime, timezone
from typing import Optional, Union

import jwt
from uuid import uuid4

from domain.services.auth import IJWTAuthService, ICookieService
from settings.dev import CommonSettings
from utils.crypto import load_private_key, load_public_key
from utils.consts.token_types import TokenTypes
from .exceptions.exceptions import JWTDecodeException

class JWTAuthService(IJWTAuthService):
    def __init__(
        self,
        settings: CommonSettings,
        cookie_service: Optional[ICookieService] = None,
    ):
        self._config = settings.jwt_settings
        self._token = None
        self._cookie = cookie_service

    def create_access_token(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str:
        return self._create_token(
            subject=subject,
            token_type=TokenTypes.ACCESS.value,
            exp_time=self.__get_expired_time(TokenTypes.ACCESS.value),
            algorithm=self._config.jwt_algorithm,
            headers=headers,
            user_claims=user_claims,
        )

    def create_refresh_token(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str:
        return self._create_token(
            subject=subject,
            token_type=TokenTypes.REFRESH.value,
            exp_time=self.__get_expired_time(TokenTypes.REFRESH.value),
            headers=headers,
            algorithm=self._config.jwt_algorithm,
            user_claims=user_claims
        )

    def decode_token(self, encoded_token: str) -> dict[str, Union[str, int, bool]]:
        try:
            return jwt.decode(
                encoded_token,
                load_public_key(self._config.jwt_public_key),
                leeway=self._config.jwt_decode_leeway,
                algorithms=[self._config.jwt_decode_algorithm],
            )
        except Exception as err:
            raise JWTDecodeException(status_code=422, message=str(err))

    def set_access_cookies(
        self,
        encoded_access_token: str,
        max_age: Optional[int] = None,
    ) -> None:
        self._cookie.set_access_cookie(encoded_access_token, max_age)

    def set_refresh_cookies(
        self,
        encoded_refresh_token: str,
        max_age: Optional[int] = None,
    ) -> None:
        self._cookie.set_refresh_cookie(encoded_refresh_token, max_age)

    def _create_token(
        self,
        subject: Union[str, int],
        token_type: str,
        user_claims: dict,
        exp_time: int,
        algorithm: str,
        headers: dict,
    ) -> str:
        claims = self.__create_claims(token_type=token_type, subject=subject, exp_time=exp_time, user_claims=user_claims)
        return jwt.encode(
            claims,
            load_private_key(self._config.jwt_private_key),
            algorithm=algorithm,
            headers=headers
        )

    def __create_claims(
        self,
        token_type: str,
        subject: str | int,
        exp_time: int,
        user_claims: dict,
    ) -> dict:
        claims = {
            "sub": subject,
            "iat": self.__get_int_from_datetime(datetime.now(timezone.utc)),
            "nbf": self.__get_int_from_datetime(datetime.now(timezone.utc)),
            "jti": self.__get_jwt_identifier(),
            "exp": exp_time,
            "type": token_type,
            "csrf": self.__get_jwt_identifier()
        }

        claims.update(user_claims)

        return claims

    @staticmethod
    def __get_jwt_identifier() -> str:
        return str(uuid4())

    @staticmethod
    def __get_int_from_datetime(value: datetime) -> int:
        return int(value.timestamp())

    def __get_expired_time(self, token_type: str,) -> int:
        match token_type:
            case "access":
                return self.__get_int_from_datetime(datetime.now(timezone.utc)) + self._config.jwt_access_token_expires
            case "refresh":
                return self.__get_int_from_datetime(datetime.now(timezone.utc)) + self._config.jwt_refresh_token_expires
