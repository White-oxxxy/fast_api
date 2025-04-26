from dataclasses import dataclass

from datetime import (
    datetime,
    timezone,
)

from domain.services.auth import (
    ICreateRefreshTokenService,
    ICreateTokenService,
)
from settings.dev import CommonSettings
from utils.consts.token_types import TokenTypes
from logic.services.auth.exceptions.exceptions import JWTDecodeException


@dataclass
class CreateRefreshTokenService(ICreateRefreshTokenService):
    create_token_service: ICreateTokenService
    settings: CommonSettings

    def execute(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str:
        return self.create_token_service.execute(
            subject=subject,
            token_type=TokenTypes.REFRESH.value,
            exp_time=self.__get_expired_time(TokenTypes.REFRESH.value),
            headers=headers,
            algorithm=self.settings.jwt_settings.jwt_algorithm,
            user_claims=user_claims
        )

    @staticmethod
    def __get_int_from_datetime(value: datetime) -> int:
        return int(value.timestamp())

    def __get_expired_time(self, token_type: str, ) -> int:
        match token_type:
            case "access":
                return self.__get_int_from_datetime(
                    datetime.now(timezone.utc)) + self.settings.jwt_settings.jwt_access_token_expires
            case "refresh":
                return self.__get_int_from_datetime(
                    datetime.now(timezone.utc)) + self.settings.jwt_settings.jwt_refresh_token_expires