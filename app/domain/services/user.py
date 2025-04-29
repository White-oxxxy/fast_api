from abc import ABC, abstractmethod

from domain.entities.user import User
from domain.repositories.user import IUserRepositoryORM


class IGetOrCreateUserService(ABC):
    repo: IUserRepositoryORM

    @abstractmethod
    async def execute(self, user: User) -> User: ...
