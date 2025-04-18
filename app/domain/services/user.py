from abc import ABC, abstractmethod

from domain.entities.user import User, UserInput


class IUserService(ABC):
    @abstractmethod
    async def get_by_username(self, user: UserInput) -> User | None: ...

    @abstractmethod
    async def create(self, user: UserInput) -> User: ...

    @abstractmethod
    async def get_or_create(self, user: UserInput) -> User | None: ...
