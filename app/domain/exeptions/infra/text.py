from dataclasses import dataclass

from .base import InfrastructureException


@dataclass
class TextAlreadyExistedException(InfrastructureException):
    @property
    def message(self):
        return "Такой текст уже существует!"


@dataclass
class TagAlreadyExistedException(InfrastructureException):
    @property
    def message(self):
        return "Такой тэг уже существует!"


@dataclass
class TextDoesntCreatedException(InfrastructureException):
    @property
    def message(self):
        return "Такой текст еще не был создан!"