from dataclasses import dataclass

from .base import RepositoryException


@dataclass
class EmptyRoleAnswer(RepositoryException):
    @property
    def message(self):
        return "Нет такой роли!"