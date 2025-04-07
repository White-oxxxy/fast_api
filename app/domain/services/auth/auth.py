from abc import ABC, abstractmethod
from datetime import timedelta

from .schemas import ABCUserSchema


class IAuthService(ABC):
    @abstractmethod
    def validate_auth_user(self, username: str, password: str): ...

    @abstractmethod
    def get_current_token_payload(self, token: str) -> dict: ...

    @abstractmethod
    def get_current_auth_user(self, payload: dict) -> ABCUserSchema: ...

    @abstractmethod
    def get_current_active_auth_user(self, user: ABCUserSchema): ...

    @abstractmethod
    def create_jwt(
        self,
        token_type: str,
        token_data: dict,
        expire_minutes: int,
        expire_timedelta: timedelta | None = None,
    ) -> str: ...

    @abstractmethod
    def create_access_token(self, user: ABCUserSchema) -> str: ...

    @abstractmethod
    def create_refresh_token(self, user: ABCUserSchema) -> str: ...
