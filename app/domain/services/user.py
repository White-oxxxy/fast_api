from abc import ABC, abstractmethod

from domain.entities.entities import User


class IUserService(ABC):
    @abstractmethod
    async def create(self, user: User) -> User: ...

    @abstractmethod
    async def get_by_id(self, user: User) -> User | None: ...

    @abstractmethod
    async def get_by_oid(self, user: User) -> User | None: ...

    @abstractmethod
    async def get_or_create(self, user: User) -> User: ...

    @abstractmethod
    async def get_by_username(self, user: User) -> User | None: ...

    @abstractmethod
    async def get_by_role(self, user: User) -> list[User] | list: ...
