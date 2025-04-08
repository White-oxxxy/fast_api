import jwt, re, uuid, hmac
from jwt.algorithms import requires_cryptography, has_crypto
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Union, Sequence
from fastapi import Request, Response

from domain.services.auth import IJWTAuthService
from settings.dev import CommonSettings


class JWTAuthService(IJWTAuthService):
    def __init__(self, settings: CommonSettings, req: Request = None, res: Response = None):
        self._config = settings
        self._token = None

        if res and self._config.jwt_settings.jwt_in_cookies:
            self._response = res

        if req:
            ...

    def create_access_token(
        self,
        subject: Union[str, int],
        fresh: Optional[bool] = False,
        algorithm: Optional[str] = None,
        headers: Optional[dict] = None,
        expires_time: Optional[Union[timedelta, int, bool]] = None,
        audience: Optional[Union[str, Sequence[str]]] = None,
        user_claims: Optional[Dict] = None
    ) -> str:
        ...


    