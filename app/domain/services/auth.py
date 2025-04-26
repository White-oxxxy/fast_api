from abc import ABC, abstractmethod
from typing import Optional, Union

from domain.entities.token import Token


class ICreateAccessTokenService(ABC):
    @abstractmethod
    def execute(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str: ...


class ICreateRefreshTokenService(ABC):
    @abstractmethod
    def execute(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str: ...


class IDecodeTokenService(ABC):
    @abstractmethod
    def execute(self, encoded_token: str) -> dict[str, Union[str, int, bool]]: ...


class ICreateTokenService(ABC):
    @abstractmethod
    def execute(
            self,
            subject: Union[str, int],
            token_type: str,
            user_claims: dict,
            exp_time: int,
            algorithm: str,
            headers: dict,
    ) -> str: ...


class ICreateClaimsService(ABC):
    @abstractmethod
    def execute(
            self,
            token_type: str,
            subject: str | int,
            exp_time: int,
            user_claims: dict,
    ) -> dict: ...


class ISetRefreshCookieService(ABC):
    @abstractmethod
    def execute(self, token: str, max_age: int | None = None) -> None: ...


class ISetAccessCookieService(ABC):
    @abstractmethod
    def execute(self, token: str, max_age: int | None = None) -> None: ...


class ITokenService(ABC):
    @abstractmethod
    async def get_or_create(self, token: Token) -> Token: ...
