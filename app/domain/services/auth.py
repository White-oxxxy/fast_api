from abc import ABC, abstractmethod
from typing import Optional, Union

from domain.entities.token import Token


class IJWTAuthService(ABC):
    @abstractmethod
    def create_access_token(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str: ...

    @abstractmethod
    def create_refresh_token(
        self,
        subject: str | int,
        headers: dict,
        user_claims: dict,
    ) -> str: ...

    @abstractmethod
    def decode_token(self, encoded_token: str) -> dict[str, Union[str, int, bool]]: ...


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


class ISetRefreshCookieService(ABC):
    @abstractmethod
    def execute(self, token: str, max_age: int | None = None) -> None: ...


class ISetAccessCookieService(ABC):
    @abstractmethod
    def execute(self, token: str, max_age: int | None = None) -> None:


class ITokenService(ABC):
    @abstractmethod
    async def get_or_create(self, token: Token) -> Token: ...
