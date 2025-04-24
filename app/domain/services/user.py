from abc import ABC, abstractmethod

from domain.entities.user import User, UserInput


class ICreateUserService(ABC):
    @abstractmethod
    async def execute(self, user: UserInput) -> User: ...


class IGetOrCreateUserService(ABC):
    @abstractmethod
    async def execute(self, user: UserInput) -> User: ...
