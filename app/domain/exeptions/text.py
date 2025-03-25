from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return "Текст не должен быть пустым!"  # noqa
