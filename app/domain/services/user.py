from abc import ABC, abstractmethod

from domain.entities.user import User
from domain.repositories.user import IUserRepositoryORM


class ICreateUserService(ABC):
    repo: IUserRepositoryORM

    @abstractmethod
    async def execute(self, user: User) -> User: ...


class IGetOrCreateUserService(ABC):
    repo: IUserRepositoryORM
    create_user_service: ICreateUserService

    @abstractmethod
    async def execute(self, user: User) -> User: ...
