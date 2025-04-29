from abc import ABC, abstractmethod

from uuid import UUID

from domain.entities.token import RefreshToken


class IRefreshTokenRepositoryORM(ABC):
    @abstractmethod
    async def get_by_oid(self, required_oid: UUID) -> RefreshToken | None: ...

    @abstractmethod
    async def create(self, refresh_token: RefreshToken) -> RefreshToken: ...

    @abstractmethod
    async def update(self, refresh_token: RefreshToken) -> RefreshToken: ...

    @abstractmethod
    async def delete(self, refresh_token: RefreshToken) -> None: ...