from dataclasses import dataclass

from domain.exeptions.base import ApplicationException


@dataclass(eq=False)
class EmptyContentException(ApplicationException):
    @property
    def message(self):
        return "Не может быть пустым!"