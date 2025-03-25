from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass(eq=False)
class EmptyNameException(ApplicationException):
    @property
    def message(self):
        return "Название роли не должно быть пустым!"  # noqa


@dataclass(eq=False)
class NameTooLongException(ApplicationException):
    @property
    def massage(self):
        return "Название не должно быть больше 255 символов!"  # noqa
