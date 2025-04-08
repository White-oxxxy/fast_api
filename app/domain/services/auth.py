from abc import ABC, abstractmethod
from typing import Optional, Union, Sequence
from fastapi import Response
from datetime import timedelta


class IJWTAuthService(ABC):
    @abstractmethod
    def create_access_token(
        self,
        subject: Union[str, int],
        fresh: Optional[bool] = False,
        algorithm: Optional[str] = None,
        headers: Optional[dict] = None,
        expires_time: Optional[Union[timedelta, int, bool]] = None,
        audience: Optional[Union[str, Sequence[str]]] = None,
        user_claims: Optional[dict] = None
    ) -> str: ...

    @abstractmethod
    def create_refresh_token(
        self,
        subject: Union[str, int],
        algorithm: Optional[str] = None,
        headers: Optional[dict] = None,
        expires_time: Optional[Union[timedelta, int, bool]] = None,
        audience: Optional[Union[str, Sequence[str]]] = None,
        user_claims: Optional[dict] = None
    ) -> str: ...

    @abstractmethod
    def set_access_cookies(
        self,
        encoded_access_token: str,
        response: Optional[Response] = None,
        max_age: Optional[int] = None
    ) -> None: ...

    @abstractmethod
    def set_refresh_cookies(
        self,
        encoded_refresh_token: str,
        response: Optional[Response] = None,
        max_age: Optional[int] = None
    ) -> None: ...

    @abstractmethod
    def unset_jwt_cookies(self, response: Optional[Response] = None) -> None: ...

    @abstractmethod
    def unset_access_cookies(self, response: Optional[Response] = None) -> None: ...

    @abstractmethod
    def unset_refresh_cookies(self, response: Optional[Response] = None) -> None: ...

    @abstractmethod
    def jwt_required(self): ...

    @abstractmethod
    def jwt_optional(self): ...

    @abstractmethod
    def jwt_refresh_token_required(self): ...

    @abstractmethod
    def fresh_jwt_required(self): ...

    @abstractmethod
    def get_raw_jwt(self): ...

    @abstractmethod
    def get_jti(self): ...

    @abstractmethod
    def get_jwt_subject(self): ...

    @abstractmethod
    def get_unverified_jwt_headers(self): ...
