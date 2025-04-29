from abc import ABC, abstractmethod

from domain.entities.token import Token
from domain.repositories.token import IRefreshTokenRepositoryORM


class IRefreshTokenCreateService(ABC):
    repo: IRefreshTokenRepositoryORM

    @abstractmethod
    async def execute(self, token: Token) -> Token: ...


class IGetOrCreateRefreshTokenService(ABC):
    repo: IRefreshTokenRepositoryORM
    refresh_token_create_service: IRefreshTokenCreateService

    @abstractmethod
    async def execute(self, token: Token) -> Token: ...
