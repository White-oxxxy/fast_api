from dataclasses import dataclass

from .base import InfrastructureException


@dataclass
class UserAlreadyExistedException(InfrastructureException):
    @property
    def message(self):
        return "Пользователь уже существует!"