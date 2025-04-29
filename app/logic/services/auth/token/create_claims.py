from dataclasses import dataclass

from datetime import datetime, timezone
from uuid import uuid4

from core.settings import CommonSettings
from domain.services.auth import ICreateClaimsService


@dataclass
class CreateClaimsService(ICreateClaimsService):
    settings: CommonSettings

    def execute(
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

    def __get_expired_time(self, token_type: str, ) -> int:
        match token_type:
            case "access":
                return self.__get_int_from_datetime(
                    datetime.now(timezone.utc)) + self.settings.jwt_settings.jwt_access_token_expires
            case "refresh":
                return self.__get_int_from_datetime(
                    datetime.now(timezone.utc)) + self.settings.jwt_settings.jwt_refresh_token_expires