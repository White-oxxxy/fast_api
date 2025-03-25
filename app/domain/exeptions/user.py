from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass(eq=False)
class EmptyUsernameException(ApplicationException):
    @property
    def message(self):
        return "Имя не должно быть пустым!"  # noqa


@dataclass(eq=False)
class UsernameTooLongException(ApplicationException):
    @property
    def message(self):
        return "Имя слишком длинное"  # noqa


@dataclass(eq=False)
class IncorrectUsernameException(ApplicationException):
    @property
    def message(self):
        return "Некорректное имя пользователя!"  # noqa
