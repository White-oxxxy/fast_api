from dataclasses import dataclass

from fastapi import Response

from domain.services.auth import (
    ISetAccessCookieService,
    IDecodeTokenService,
)
from core.settings import CommonSettings


@dataclass
class CookieService(ISetAccessCookieService):
    decode_token_service: IDecodeTokenService
    settings: CommonSettings
    response: Response

    def execute(
        self, encoded_access_token: str, max_age: int | None = None
    ) -> None:
        self.response.set_cookie(
            self.settings.jwt_settings.jwt_access_csrf_cookie_key,
            self.decode_token_service.execute(encoded_access_token)["csrf"],
            max_age=max_age,
            path=self.settings.jwt_settings.jwt_access_csrf_cookie_path,
            domain=self.settings.jwt_settings.jwt_cookie_domain,
            secure=self.settings.jwt_settings.jwt_cookie_secure,
            httponly=False,
            samesite=self.settings.jwt_settings.jwt_cookie_samesite,
        )

