from dataclasses import dataclass

from fastapi import Response

from domain.services.auth import (
    ISetRefreshCookieService,
    IDecodeTokenService,
)
from core.settings import CommonSettings


@dataclass
class SetRefreshCookieService(ISetRefreshCookieService):
    decode_token_service: IDecodeTokenService
    response: Response
    settings: CommonSettings

    def execute(
            self, encoded_refresh_token: str, max_age: int | None = None
    ) -> None:
        self.response.set_cookie(
            self.settings.jwt_settings.jwt_refresh_csrf_cookie_key,
            self.decode_token_service.execute(encoded_refresh_token)["csrf"],
            max_age=max_age,
            path=self.settings.jwt_settings.jwt_refresh_csrf_cookie_path,
            domain=self.settings.jwt_settings.jwt_cookie_domain,
            secure=self.settings.jwt_settings.jwt_cookie_secure,
            httponly=False,
            samesite=self.settings.jwt_settings.jwt_cookie_samesite,
        )