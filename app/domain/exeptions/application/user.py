from dataclasses import dataclass

from domain.exeptions.application.base import ApplicationException


@dataclass
class EmptyNameException(ApplicationException):
    @property
    def message(self):
        return 'Никнейм не может быть пустым!'


@dataclass
class NameTooLongException(ApplicationException):
    @property
    def message(self):
        return 'Длина никнейма не должна быть больше 15 символов!'


@dataclass
class EmptyPasswordException(ApplicationException):
    @property
    def message(self):
        return 'Пароль не может быть пустым!'


@dataclass
class EmptyEmailException(ApplicationException):
    @property
    def message(self):
        return "Почта не может быть пустой!"


@dataclass
class IncorrectEmailFormatException(ApplicationException):
    @property
    def message(self):
        return "Неверный формат почты!"


@dataclass
class EmptyRoleException(ApplicationException):
    @property
    def message(self):
        return "Роль не может быть пустой!"