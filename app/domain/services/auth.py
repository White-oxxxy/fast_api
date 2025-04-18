from abc import ABC, abstractmethod
from typing import Optional, Union


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

    @abstractmethod
    def set_access_cookies(
        self,
        encoded_access_token: str,
        max_age: Optional[int] = None,
    ) -> None: ...

    @abstractmethod
    def set_refresh_cookies(
        self,
        encoded_refresh_token: str,
        max_age: Optional[int] = None,
    ) -> None: ...


class ICookieService(ABC):
    @abstractmethod
    def set_access_cookie(self, token: str, max_age: int | None = None) -> None: ...

    @abstractmethod
    def set_refresh_cookie(self, token: str, max_age: int | None = None) -> None: ...


class ITokenService(ABC):
    @abstractmethod
    async def create(self): ...

    @abstractmethod
    async def get(self): ...

    @abstractmethod
    async def get_or_create(self): ...