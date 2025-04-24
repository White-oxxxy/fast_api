from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.user import User, UserInput
from domain.repositories.base import IBaseRepositoryORM


class IUserRepositoryORM(IBaseRepositoryORM, ABC):
    @abstractmethod
    async def create(self, user: UserInput) -> User: ...

    @abstractmethod
    async def get_by_oid(self, required_oid: UUID) -> User | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None: ...