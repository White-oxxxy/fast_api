from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.user import User
from domain.repositories.base import IBaseRepositoryORM


class IUserRepositoryORM(IBaseRepositoryORM, ABC):
    @abstractmethod
    async def create(self, user: User) -> User: ...

    @abstractmethod
    async def get_by_oid(self, required_oid: UUID) -> User | None: ...