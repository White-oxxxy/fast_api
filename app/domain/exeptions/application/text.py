from dataclasses import dataclass

from domain.exeptions.application.base import ApplicationException


@dataclass
class EmptyTagNameException(ApplicationException):
    @property
    def message(self):
        return "Тэг не может быть пустым!"


@dataclass
class IncorrectTagFormatException(ApplicationException):
    @property
    def message(self):
        return "Неверный формат тэга!"


@dataclass
class TagTooLongException(ApplicationException):
    @property
    def message(self):
        return "Длина тэга не может быть больше 15 символов!"


@dataclass
class EmptyTextValueException(ApplicationException):
    @property
    def message(self):
        return "Текст не может быть пустым!"