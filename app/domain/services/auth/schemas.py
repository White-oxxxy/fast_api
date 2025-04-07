from abc import ABC, abstractmethod


class ABCUserSchema(ABC):
    @property
    @abstractmethod
    def username(self) -> str: ...

    @property
    @abstractmethod
    def password(self) -> str: ...

    @property
    @abstractmethod
    def email(self) -> str: ...

    @property
    @abstractmethod
    def active(self) -> str: ...
