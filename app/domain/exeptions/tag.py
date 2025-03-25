from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass(eq=False)
class IncorrectTagPrefixException(ApplicationException):
    @property
    def message(self):
        return "Тэг должен начинаться с #"  # noqa


@dataclass(eq=False)
class EmptyTagNameException(ApplicationException):
    @property
    def message(self):
        return "Тэг не должен быть пустым!"  # noqa


@dataclass(eq=False)
class TagTooLongException(ApplicationException):
    @property
    def message(self):
        return "Длина тэга не должна быть больше 255"  # noqa


@dataclass(eq=False)
class InvalidSeparatorBetweenTagsException(ApplicationException):
    @property
    def message(self):
        return "Формат ввода нескольких тэгов: #tag1, #tag2"  # noqa
