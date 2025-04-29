from dataclasses import dataclass

from .base import ApplicationException


@dataclass
class EmptyTokenException(ApplicationException):
    @property
    def message(self):
        return "Токен не может быть пустым!"


@dataclass
class EmptyIpAddressException(ApplicationException):
    @property
    def message(self):
        return "Адресс не может быть пустым!"


@dataclass
class IncorrectIpAddressException(ApplicationException):
    @property
    def message(self):
        return "Неверный формат айпи адрсса"


@dataclass
class EmptyUserAgentException(ApplicationException):
    @property
    def message(self):
        return "Юзер агент не может быть пустым!"